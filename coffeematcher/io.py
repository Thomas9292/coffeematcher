import os
import pickle

from typing import Dict, List


def load_memory_from_file(memory_file: str) -> Dict[str, List[str]]:
    """Loads memory from file and unpickles it. If no memory file is found, empty memory is returned.

    Args:
        memory_file (str): path to memory file

    Returns:
        Dict[str, List[str]]: Memory file
    """
    try:
        with open(memory_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError as e:
        return dict()


def save_memory_to_file(memory: Dict[str, List[str]], memory_file: str, backup=True):
    """Pickles memory and saves it to file

    Args:
        memory (Dict[str, List[str]]): memory dictionary to be saved
        memory_file (str): path to save file
        backup (bool): if true, creates backup as file with '_backup' suffix
    """
    if backup:
        try:
            with open(memory_file, "rb") as file:
                old_content = pickle.load(file)
            backup_path = memory_file + "_backup"
            save_memory_to_file(old_content, backup_path, backup=False)
        except FileNotFoundError as e:
            pass
    with open(memory_file, "wb") as file:
        pickle.dump(memory, file, protocol=pickle.HIGHEST_PROTOCOL)


def load_participants_from_file(participants_file: str) -> str:
    """Reads .txt file with contents copy pasted from teams list

    Args:
        participants_file (str): location of participants file

    Returns:
        str: raw contents of participants file
    """
    with open(participants_file, "r") as file:
        data = file.read()
    return data
