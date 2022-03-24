from typing import Dict, List, Tuple

EMAIL_TEMPLATE = """Hi all!

This is another round of random coffee matches! Below you will find the matches, we ask the person on the left to take the initiative to set a time! The next round of coffee matches will go out on <CHANGE_DATE>, so make to sure plan it before then.

{match_block}

All the best,

Azamat & Thomas
"""


def format_email(matches: List[Tuple[str, str]], participants: Dict[str, str]) -> str:
    # TODO: properly format email
    matches_strings = [format_match(match, participants) for match in matches]
    match_block = "\n".join(matches_strings)

    return EMAIL_TEMPLATE.format(match_block=match_block)


def format_email_recipients(participants: Dict[str, str]) -> str:
    """Formats email addresses ready to be pasted in outloo

    Args:
        participants (Dict[str, str]): dictionary of participants (email -> name)

    Returns:
        str: formatted string with participant emails
    """
    return ", ".join(participants.keys())


def format_match(match: Tuple[str, str], participants: Dict[str, str]) -> str:
    participant_1 = f"{participants[match[0]]} ({match[0]})"
    participant_2 = f"{participants[match[1]]} ({match[1]})"
    return f"{participant_1:<65} -   {participant_2}"
