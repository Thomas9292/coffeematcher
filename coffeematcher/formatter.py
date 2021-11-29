from typing import List, Tuple


def format_email(matches: List[Tuple[str, str]]) -> str:
    # TODO: properly format email
    return "Hi. This is the email.\n\nMatches:\n\n" + "\n".join(
        [" - ".join(match) for match in matches]
    )


def format_email_recipients(participants: List[str]) -> str:
    return ", ".join(participants)
