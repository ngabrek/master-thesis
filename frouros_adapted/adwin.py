"""ADWIN (ADaptive WINdowing) module."""

from collections import deque
from typing import List, Optional, Union

import numpy as np  # type: ignore

from frouros.callbacks.streaming.base import BaseCallbackStreaming
from frouros.detectors.concept_drift.streaming.window_based.base import (
    BaseWindowConfig,
    BaseWindow,
)

class Bucket:
    def __init__(self, m: int) -> None:
        self.array_size = m + 1
        self.total = np.zeros(self.array_size)
        self.variance = np.zeros(self.array_size)
        self.idx = 0

    @property
    def array_size(self) -> int:
        return self._array_size

    @array_size.setter
    def array_size(self, value: int) -> None:
        if value < 2:
            raise ValueError("array_size value must be greater than 1.")
        self._array_size = value

    @property
    def total(self) -> np.ndarray:
        return self._total

    @total.setter
    def total(self, value: np.ndarray) -> None:
        if not isinstance(value, np.ndarray):
            raise TypeError("value must be of type numpy.ndarray.")
        self._total = value

    @property
    def variance(self) -> np.ndarray:
        return self._variance

    @variance.setter
    def variance(self, value: np.ndarray) -> None:
        if not isinstance(value, np.ndarray):
            raise TypeError("value must be of type numpy.ndarray.")
        self._variance = value

    @property
    def idx(self) -> int:
        return self._idx

    @idx.setter
    def idx(self, value: int):
        if value < 0:
            raise ValueError("idx value must be greater or equal than 0.")
        self._idx = value

    def reset(self) -> None:
        self.total = np.zeros(self.array_size)
        self.variance = np.zeros(self.array_size)

    def insert_data(self, value: float, variance: float) -> None:
        self.total[self.idx] = value
        self.variance[self.idx] = variance
        self.idx += 1

    def remove(self) -> None:
        self.compress(num_items_deleted=1)

    def compress(self, num_items_deleted: int) -> None:
        for i in range(num_items_deleted, self.array_size):
            idx = i - num_items_deleted
            self.total[idx] = self.total[i]
            self.variance[idx] = self.variance[i]

        idx_start = self.array_size - num_items_deleted
        # fmt: off
        self.total[idx_start:self.array_size] = 0.0
        self.variance[idx_start:self.array_size] = 0.0
        # fmt: on

        self.idx -= num_items_deleted


class ADWINConfig(BaseWindowConfig):

    def __init__(  # noqa: D107
        self,
        clock: int = 32,
        delta: float = 0.002,
        m: int = 5,
        min_window_size: int = 5,
        min_num_instances: int = 10,
    ) -> None:
        super().__init__(min_num_instances=min_num_instances)
        self.clock = clock
        self.delta = delta
        self.m = m
        self.min_window_size = min_window_size

    @property
    def clock(self) -> int:
        return self._clock

    @clock.setter
    def clock(self, value: int) -> None:
        if value < 0:
            raise ValueError("clock value must be greater than 0.")
        self._clock = value

    @property
    def delta(self) -> float:
        return self._delta

    @delta.setter
    def delta(self, value: float) -> None:
        if not 0 < value < 1:
            raise ValueError("delta value must be in the range (0, 1).")
        self._delta = value

    @property
    def m(self) -> int:
        return self._m

    @m.setter
    def m(self, value: int) -> None:
        if value < 1:
            raise ValueError("m value must be greater than 0.")
        self._m = value

    @property
    def min_window_size(self) -> int:
        return self._min_window_size

    @min_window_size.setter
    def min_window_size(self, value: int) -> None:
        if value < 1:
            raise ValueError("min_window_size value must be greater than 0.")
        self._min_window_size = value

class ADWIN(BaseWindow):
    config_type = ADWINConfig

    def __init__(  
        self,
        config: Optional[ADWINConfig] = None,
        callbacks: Optional[
            Union[BaseCallbackStreaming, List[BaseCallbackStreaming]]
        ] = None,
    ) -> None:
        super().__init__(
            config=config,
            callbacks=callbacks,
        )
        num_buckets = 0
        self.additional_vars = {
            "buckets": deque([Bucket(m=self.config.m)]),  # type: ignore
            "total": 0.0,
            "variance": 0.0,
            "width": 0,
            "num_buckets": num_buckets,
            "num_max_buckets": num_buckets,
        }
        self._set_additional_vars_callback()
        self._min_instances = self.config.min_num_instances + 1
        #adaption: attribute added 
        self.drift_detected = False 

    @property
    def buckets(self) -> deque:
        return self._additional_vars["buckets"]

    @buckets.setter
    def buckets(self, value: deque):
        if not isinstance(value, deque):
            raise TypeError("value must be of type deque.")
        self._additional_vars["buckets"] = value

    @property
    def total(self) -> float:
        return self._additional_vars["total"]

    @total.setter
    def total(self, value: float) -> None:
        if value < 0.0:
            raise ValueError("total value must be greater or equal than 0.0.")
        self._additional_vars["total"] = value

    @property
    def variance(self) -> float:
        return self._additional_vars["variance"]

    @variance.setter
    def variance(self, value: float) -> None:
        self._additional_vars["variance"] = value

    @property
    def variance_window(self) -> float:
        return self.variance / self.width

    @property
    def width(self) -> int:
        return self._additional_vars["width"]

    @width.setter
    def width(self, value: int) -> None:
        if value < 0:
            raise ValueError("width value must be greater or equal than 0.")
        self._additional_vars["width"] = value

    @property
    def num_buckets(self) -> int:
        return self._additional_vars["num_buckets"]

    @num_buckets.setter
    def num_buckets(self, value: int) -> None:
        if value < 0:
            raise ValueError("num_buckets value must be greater or equal than 0.")
        self._additional_vars["num_buckets"] = value

    @property
    def num_max_buckets(self) -> int:
        return self._additional_vars["num_max_buckets"]

    @num_max_buckets.setter
    def num_max_buckets(self, value: int) -> None:
        if value < 0:
            raise ValueError("num_max_buckets value must be greater or equal than 0.")
        self._additional_vars["num_max_buckets"] = value

    def _insert_bucket(self, value: float) -> None:
        self._insert_bucket_data(variance=0.0, value=value, bucket=self.buckets[0])
        self.width += 1
        incremental_variance = (
            (self.width - 1)
            * (value - self.total / (self.width - 1))
            * (value - self.total / (self.width - 1))
            / self.width
            if self.width > 1
            else 0.0
        )
        self.variance += incremental_variance
        self.total += value
        self._compress_buckets()

    def _insert_bucket_data(
        self, value: float, variance: float, bucket: Bucket
    ) -> None:
        bucket.insert_data(value=value, variance=variance)
        self.num_buckets += 1
        if self.num_buckets > self.num_max_buckets:
            self.num_max_buckets = self.num_buckets

    @staticmethod
    def _bucket_size(index: int) -> int:
        return np.power(2, index)

    def _delete_bucket(self) -> int:
        bucket = self.buckets[-1]
        bucket_size = self._bucket_size(index=len(self.buckets) - 1)
        self.width -= bucket_size
        self.total -= bucket.total[0]
        bucket_mean = bucket.total[0] / bucket_size
        window_mean = self.total / self.width
        incremental_variance = bucket.variance[0] + bucket_size * self.width * (
            bucket_mean - window_mean
        ) * (bucket_mean - window_mean) / (bucket_size + self.width)
        self.variance -= incremental_variance

        bucket.remove()
        self.num_buckets -= 1
        if bucket.idx == 0:
            self.buckets.pop()

        return bucket_size

    def _compress_buckets(self) -> None:
        bucket = self.buckets[0]
        idx = 0
        while bucket is not None:
            idx_next = idx + 1
            if bucket.idx == bucket.array_size:
                try:
                    next_bucket = self.buckets[idx_next]
                except IndexError:
                    self.buckets.append(Bucket(m=self.config.m))  # type: ignore
                    next_bucket = self.buckets[-1]
                bucket_size = self._bucket_size(index=idx)
                bucket_1_mean, bucket_2_mean = bucket.total[0:2] / bucket_size
                incremental_variance = (
                    bucket_size
                    * bucket_size
                    * (bucket_1_mean - bucket_2_mean)
                    * (bucket_1_mean - bucket_2_mean)
                    / (bucket_size * 2)
                )
                total = np.sum(bucket.total[0:2])
                variance = np.sum(bucket.variance[0:2]) + incremental_variance
                next_bucket.insert_data(value=total, variance=variance)
                self.num_buckets += 1
                bucket.compress(num_items_deleted=2)

                if next_bucket.idx <= self.config.m:  # type: ignore
                    break
            else:
                break

            try:
                bucket = self.buckets[idx_next]
            except IndexError:
                bucket = None
            idx += 1

    def _calculate_threshold(self, w0_instances: int, w1_instances: int) -> float:
        delta_prime = np.log(2 * np.log(self.width) / self.config.delta)  # type: ignore
        # Has highlighted in river library, the use of the reciprocal
        # of m allows to avoid extra divisions
        min_window_size = self.config.min_window_size + 1  # type: ignore
        m_reciprocal = 1 / (w0_instances - min_window_size) + 1 / (
            w1_instances - min_window_size
        )
        epsilon = (
            np.sqrt(2 * m_reciprocal * self.variance_window * delta_prime)
            + 2 / 3 * delta_prime * m_reciprocal
        )
        return epsilon

    def _update(self, value: Union[int, float], **kwargs) -> None:
        #adaption: reset added, if a drift was detected 
        if self.drift:
            self.reset()
            self.drift_detected = self.drift
            
        self.num_instances += 1
        self._insert_bucket(value=value)

        if (
            self.num_instances % self.config.clock == 0  # type: ignore
            and self.width > self.config.min_num_instances  # type: ignore
        ):
            flag_reduce_width = True

            while flag_reduce_width:
                flag_reduce_width = False
                flag_exit = False
                w0_instances = 0
                w1_instances = self.width
                w0_total = 0
                w1_total = self.total

                for i in range(len(self.buckets) - 1, -1, -1):
                    if flag_exit:
                        break
                    bucket = self.buckets[i]
                    for j in range(bucket.idx - 1):
                        bucket_size = self._bucket_size(index=i)

                        w0_instances += bucket_size
                        w1_instances -= bucket_size
                        w0_total += bucket.total[j]
                        w1_total -= bucket.total[j]

                        if i == 0 and j == bucket.idx - 1:
                            flag_exit = True
                            break

                        if (
                            w1_instances > self.config.min_window_size  # type: ignore
                            and (
                                w0_instances
                                > self.config.min_window_size  # type: ignore
                            )
                        ):
                            w0_mean = w0_total / w0_instances
                            w1_mean = w1_total / w1_instances
                            threshold = self._calculate_threshold(
                                w0_instances=w0_instances, w1_instances=w1_instances
                            )
                            if np.abs(w0_mean - w1_mean) > threshold:
                                # Drift detected
                                flag_reduce_width = True
                                self.drift = True
                                #adaption: update of attribute
                                self.drift_detected = self.drift 
                                if self.width > 0:
                                    w0_instances -= self._delete_bucket()
                                    flag_exit = True
                                    break
                                    

    def reset(self) -> None:
        super().reset()
        self.buckets = deque([Bucket(m=self.config.m)])  # type: ignore
        self.total = 0.0
        self.variance = 0.0
        self.width = 0
        self.num_buckets = 0
        self.num_max_buckets = self.num_buckets