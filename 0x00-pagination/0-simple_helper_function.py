#!/usr/bin/env python3
"""
0-simple_helper_function module
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of size two containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
