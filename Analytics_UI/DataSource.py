class DataSource:
    def fetch():
        pass


import numpy as np


class FixedDataSource(DataSource):
    def fetch():
        return [np.random.randint(1, 20) for i in range(100)]
