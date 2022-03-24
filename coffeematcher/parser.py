from typing import Dict


def parse_participants(participants_raw: str) -> Dict[str, str]:
    """Parses contents of teams table (copy pasted to a string) with following headers: First name, Last name, Email address.

    Args:
        participants_raw (str): raw content of the teams table in string

    Returns:
        Dict[str, str]: dictionary of participants (email address -> name)
    """
    participants = {}
    lines = participants_raw.split("\n")

    for line in lines:
        if not line.split() or line == "First name\tLast name\tEmail address":
            continue

        components = line.split("\t")
        name = " ".join(components[:-1])
        email = components[-1]

        participants[email] = name

    return participants
