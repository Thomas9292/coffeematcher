import os

from coffeematcher.formatter import format_email, format_email_recipients
from coffeematcher.io import load_participants_from_file
from coffeematcher.matcher import match_participants
from coffeematcher.parser import parse_participants

data_dir = os.path.join(os.path.split(os.path.dirname(__file__))[0], "data")
memory_file = os.path.join(data_dir, "memory.pickle")
participants_file = os.path.join(data_dir, "teams_participants.txt")


def main():
    participants_raw = load_participants_from_file(participants_file)
    participants = parse_participants(participants_raw)
    matches = match_participants([*participants], memory_file)

    email_body = format_email(matches, participants)
    recipients = format_email_recipients(participants)

    print(recipients, end="\n\n-----\n\n")
    print(email_body)


if __name__ == "__main__":
    main()
