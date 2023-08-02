import subprocess
from typing import Optional

from sesame.logging import logger


def run_system_command(cmd: str) -> Optional[str]:
    try:
        completed_process = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True,
        )
        return completed_process.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
