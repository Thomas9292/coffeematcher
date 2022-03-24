import random
from typing import Dict, List, Tuple

from coffeematcher.io import load_memory_from_file, save_memory_to_file
from coffeematcher.utils import MatchingError

max_mem_size = 4


def match_participants(
    participants: List[str], memory_file: str
) -> List[Tuple[str, ...]]:
    """Match participants to participants they were not recently matched to, and themselves

    Args:
        participants (List[str]): list of participants
        memory_file (str): file path of memory file

    Returns:
        List[Tuple[str, ...]]: Matched participants in duo's and potentially one trio (in odd situation)

    Throws:
        MatchingError: If non-deterministic matching algorithm doesn't supply a viable solution
    """
    memory = load_memory_from_file(memory_file)
    memory = prepare_memory_with_particants(participants, memory)

    to_be_matched = participants.copy()
    matches: List[Tuple[str, ...]] = []

    # While there are still people to be matched
    while len(to_be_matched) > 1:
        # Pick a random person and obtain potential matches
        personA = random.choice(to_be_matched)
        match_pool = get_match_pool(to_be_matched, personA, max_mem_size, memory)

        # If a deadlock is reached, return not succesful (TODO: change to throwing error)
        if len(match_pool) == 0:
            raise MatchingError

        # Pick the match, remove matched duo from match pool and update the memory
        personB = random.choice(match_pool)
        to_be_matched.remove(personA)
        to_be_matched.remove(personB)
        matches.append((personA, personB))
        memory[personA].append(personB)
        memory[personB].append(personA)

    # When odd number of participants, add final participant to last duo and update memory
    if len(to_be_matched) == 1:
        matches[-1] = (matches[-1][0], matches[-1][1], to_be_matched[0])
        memory[to_be_matched[0]].append(matches[-1][0])
        memory[to_be_matched[0]].append(matches[-1][1])
        memory[matches[-1][0]].append(to_be_matched[0])
        memory[matches[-1][1]].append(to_be_matched[0])

    save_memory_to_file(memory, memory_file)
    return matches


def prepare_memory_with_particants(
    participants: List[str], memory: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    """Prepare memory by populating memory with first time participants

    Args:
        participants (List[str]): List of participants
        memory (Dict[str, List[str]]): Unprepared memory dictionary

    Returns:
        Dict[str, List[str]]: Memory dictionary with entries for every participant
    """
    for participant in participants:
        if participant not in memory:
            memory[participant] = []
    return memory


def get_match_pool(
    to_be_matched: List[str],
    personA: str,
    max_mem_size: int,
    memory: Dict[str, List[str]],
) -> List[str]:
    """Generate match pool with previously matched persons and the person him/herself

    Args:
        to_be_matched (List[str]): List of people who still need to be matched
        personA (str): The person for who a match needs to be found
        max_mem_size (int): The maximum number of previously matched people to ignore as possible matches
        memory (Dict[str, List[str]]): Dictionary with people as key and previous matches in a list as value

    Returns:
        List[str]: List of possible matches
    """
    # Convert potential matches and self to sets for faster subtraction and deduplication
    to_be_matched_set = set(to_be_matched)
    self_set = set((personA,))

    # Determine recent memory by taking the maximum memory size or the size of the memory, whichever is smallest
    if max_mem_size == 0:
        recent_memory_set = set()
    else:
        mem_index = max(-max_mem_size, -len(memory[personA]))
        recent_memory = memory[personA][mem_index:]
        recent_memory_set = set(recent_memory)

    # Remove self and recent matches and return
    return list(to_be_matched_set - self_set - recent_memory_set)
