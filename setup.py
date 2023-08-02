from setuptools import setup, find_packages

setup(
    name="sesame",
    version="1.1.3",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=5.4",
    ],
    entry_points={
        "console_scripts": [
            "sesame=sesame.sesame:main_cli",
        ],
    },
)
