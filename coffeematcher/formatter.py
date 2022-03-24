from typing import Dict, List, Tuple


def format_email(matches: List[Tuple[str, str]]) -> str:
    # TODO: properly format email
    return "Hi. This is the email.\n\nMatches:\n\n" + "\n".join(
        [" - ".join(match) for match in matches]
    )


def format_email_recipients(participants: Dict[str, str]) -> str:
    """Formats email addresses ready to be pasted in outloo

    Args:
        participants (Dict[str, str]): dictionary of participants (email -> name)

    Returns:
        str: formatted string with participant emails
    """
    return ", ".join(participants.keys())
