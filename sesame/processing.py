import concurrent.futures
from typing import List

from sesame.system import run_system_command
from sesame.utils import SECRET, YAML


def _run_kubeseal(key: str, value: str, namespace: str, secret: str) -> SECRET:
    cmd = f'echo -n "{value}" | kubeseal --raw --name {secret} -n {namespace}'
    return {key: run_system_command(cmd).strip()}


def seal_secrets(raw_secrets: YAML, namespace: str, secret: str) -> List[SECRET]:
    sealed_secrets = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(_run_kubeseal, key, value, namespace, secret)
            for key, value in raw_secrets.items()
        ]
        for future in concurrent.futures.as_completed(futures):
            sealed_secret = future.result()
            sealed_secrets.append(sealed_secret)
    return sealed_secrets
