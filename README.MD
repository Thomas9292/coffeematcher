# coffeematcher

coffeematcher is a python library to randomly match participants for coffee meetings.

## Installation

Clone the repository:
```bash
git clone https://github.com/Thomas9292/coffeematcher.git
```

Navigate to the project folder and use [pip](https://pip.pypa.io/en/stable/) to install coffeematcher.

```bash
pip install -e .
```

## Usage
Paste the contents of a table copied from teams in a file: `data/teams_participants.txt`. The table should have the following contents

<table>
  <tr>
    <td>First name</td>
    <td>Last name</td>
    <td>Email address</td>
  </tr>
  <tr>
    <td>Thomas</td>
    <td>Wesselink</td>
    <td>email@example.com</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
</table>

#### Run the script
```bash
run_coffee
```
