from typing import List

from coffeematcher.io import load_participants_from_file

def parse_participants(participants_file: str) -> List[str]:
  participants_raw = load_participants_from_file(participants_file)
  # TODO: implement parsing function
  return ["participant1@example.com", "participant2@example.com"]
