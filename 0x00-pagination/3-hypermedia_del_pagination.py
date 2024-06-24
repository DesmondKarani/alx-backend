#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination information

        Args:
            index (int): The current start index of the return page.
            page_size (int): The current page size.

        Returns:
            dict: A dictionary containing pagination information.
        """
        assert isinstance(index, int) and index >= 0, "index must be a
        non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must
        be a positive integer"

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index < total_items, "index must be within range"

        data = []
        current_index = index

        while len(data) < page_size and current_index < total_items:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < total_items else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }