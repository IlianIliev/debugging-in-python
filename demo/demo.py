import dataclasses
import json

from pathlib import Path
from typing import Optional

import requests


BASE_DIR = Path(__file__).resolve().parent.parent


@dataclasses.dataclass
class User:
    name: str
    age: int
    website: str
    website_is_valid: Optional[bool] = None

    def __str__(self):
        return f'{self.name} ({self.age}) - {self.website}'

    def __post_init__(self):
        if not self.website.startswith('http'):
            self.website_is_valid = False

        response = requests.head(self.website)
        self.website_is_valid = response.ok


def load_file(path):
    with open(BASE_DIR / path, 'r') as f:
        return f.read()


def parse_item(item):
    params = {key: value for key, value in item.items() if key in User.__dataclass_fields__}
    return User(**params)


def main():
    import pdb; pdb.set_trace()

    json_content = load_file('data.json')
    data = json.loads(json_content)

    users = [parse_item(item) for item in data]

    for user in users:
        print(user)


if __name__ == '__main__':
    main()
