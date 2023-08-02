import logging
from pathlib import Path

root_dir = Path(__file__).parent.parent.absolute()
log_level = logging.INFO
output_file = "sealedsecrets.yaml"
