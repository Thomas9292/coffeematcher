from typing import List

from coffeematcher.io import load_participants_from_file


def parse_participants(participants_raw: str) -> List[str]:
    # TODO: implement parsing function
    return participants_raw.split()
