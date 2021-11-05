import os
from typing import List, Tuple

from coffeematcher.formatter import format_email, format_email_recipients
from coffeematcher.matcher import match_participants
from coffeematcher.parser import parse_participants

data_dir = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'data')
memory_file = os.path.join(data_dir, 'memory.pickle')
participants_file = os.path.join(data_dir,'participants.txt')

def main():
  participants = parse_participants(participants_file)
  matches = match_participants(participants, memory_file)

  email_body = format_email(matches)
  recipients = format_email_recipients(participants)

  print(recipients, end="\n\n-----\n\n")
  print(email_body)

if __name__ == "__main__":
  main()
