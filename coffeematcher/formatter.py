from typing import List, Tuple

def format_email(matches: List[Tuple[str, str]]) -> str:
  return "Hi. This is the email."

def format_email_recipients(participants: List[str]) -> str:
  return ', '.join(['joe@example.com', 'mary@abc.com'])