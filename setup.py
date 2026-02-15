from setuptools import setup, find_packages

setup(
    name="log-analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "log-analyzer=log_analyzer.cli:main",
        ],
    },
)