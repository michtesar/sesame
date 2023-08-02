import argparse
from argparse import Namespace


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Seal Kubernetes secrets from YAML file with raw secrets"
    )
    parser.add_argument(
        "-i",
        "--input_file",
        required=True,
        type=str,
        help="The input .yaml file with the raw secrets",
    )
    parser.add_argument(
        "-c",
        "--context",
        required=True,
        type=str,
        help="Kubernetes context, for example 'prod-eu'",
    )
    parser.add_argument(
        "-n",
        "--namespace",
        required=True,
        type=str,
        help="Kubernetes namespace, for example 'prod'",
    )
    parser.add_argument(
        "-s",
        "--secret",
        required=True,
        type=str,
        help="Secret name, for example 'maprd'",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        default="sealedsecrets.yaml",
        type=str,
        help="The output file with the sealed secrets",
    )
    return parser.parse_args()
