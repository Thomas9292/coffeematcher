import os
import pickle

from typing import Dict, List


def load_memory_from_file(memory_file: str) -> Dict[str, List[str]]:
    try:
        with open(memory_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError as e:
        return dict()


def save_memory_to_file(memory: Dict[str, List[str]], memory_file: str):
    with open(memory_file, "wb") as file:
        pickle.dump(memory, file, protocol=pickle.HIGHEST_PROTOCOL)


def load_participants_from_file(participants_file: str) -> str:
    # TODO: implement function
    with open(participants_file, "r") as file:
        data = file.read()
    return data
