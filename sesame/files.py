from pathlib import Path
from typing import List

import yaml

from sesame.utils import SECRET, YAML


def load_from_yaml(path: Path) -> YAML:
    with open(path, "r") as file:
        yaml_data = yaml.safe_load(file)
        return yaml_data


def save_to_yaml(sealed_secrets: List[SECRET], output_file: str) -> None:
    with open(output_file, "w") as file:
        yaml.dump(sealed_secrets, file, default_flow_style=False)
