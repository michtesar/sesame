from sesame.logging import logger
from sesame.system import run_system_command


def _set_namespace(namespace: str) -> bool:
    output = run_system_command(f"kubens {namespace}")
    if not output.split("\n")[-1].strip() == f'Active namespace is "{namespace}".':
        raise ValueError(output)
    logger.info(f"Switched to Kubernetes namespace: '{namespace}'")
    return True


def _set_context(context: str) -> bool:
    output = run_system_command(f"kubectx {context}")
    if not output == f'Switched to context "{context}".':
        raise ValueError(output)
    logger.info(f"Switched to Kubernetes context: '{context}'")
    return True


def setup_kubernetes(context: str, namespace: str) -> bool:
    return _set_context(context) and _set_namespace(namespace)
