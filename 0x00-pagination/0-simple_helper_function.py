#!/usr/bin/env python3
"""simple Helper Function"""
from typing import Tuple
def index_range(page:int, page_size:int) -> Tuple[int,int]:
    """A function that takes in the page and page size"""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
