import requests
import logging
from typing import List, Dict
from setup import MRBEAM_API


# TODO: make it asynchronous
def random_beam(complexity: str = "elementary", units_count: int = 0) -> List[Dict]:
    """
    Make request to the mister beam API and return a random beam.

    Args:
        complexity (str): complexity of the beam.
        units_count (int): number of units beam contains.

    Returns:
        random_beam (List(Dict))
    """
    response = requests.post(
        MRBEAM_API,
        data={
            "complexity": complexity,
            "unitsCount": units_count
        })

    if response.status_code == 200:
        random_beam = response.json()
    else:
        random_beam = []
    return random_beam

