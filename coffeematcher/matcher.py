from typing import Dict, List, Tuple

from coffeematcher.io import load_memory_from_file, save_memory_to_file

def match_participants(participants: List[str], memory_file: str) -> List[Tuple[str, str]]:
  memory = load_memory_from_file(memory_file)
  memory = prepare_memory_with_particants(participants, memory)

  save_memory_to_file(memory, memory_file)

  # TODO: implement matching
  return [(participants[0], participants[1]),]

def prepare_memory_with_particants(participants: List[str], memory: Dict[str, List[str]]):
  for participant in participants:
    if participant not in memory:
      memory[participant] = []
  return memory