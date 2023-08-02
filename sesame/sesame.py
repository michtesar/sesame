from sesame.args import parse_arguments
from sesame.files import load_from_yaml, save_to_yaml
from sesame.kubernetes import setup_kubernetes
from sesame.processing import seal_secrets
from sesame.utils import remove_empty_variables, remove_nested_variables


def main_cli() -> None:
    args = parse_arguments()
    secrets = load_from_yaml(args.input_file)
    setup_kubernetes(args.context, args.namespace)
    remove_nested_variables(secrets)
    remove_empty_variables(secrets)
    sealed_secretes = seal_secrets(secrets, args.namespace, args.secret)
    save_to_yaml(sealed_secretes, args.output_file)
