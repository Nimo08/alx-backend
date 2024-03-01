#!/usr/bin/env python3
"""
Simple helper function
When page numbers are 1-indexed, page - 1 is used to
align with the 0-indexed nature of lists & arrays.
"""

from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Simple pagination
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer > 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page_size must be an integer > 0"
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset) or end_index > len(dataset):
            return []
        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
