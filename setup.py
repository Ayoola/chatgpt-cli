from setuptools import setup, find_packages

setup(
    name="chatgpt-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'chatgpt=chatgpt_cli.cli:main',
        ],
    },
    description="A simple command line interface for ChatGPT",
    keywords="chatgpt, cli, openai",
    python_requires=">=3.6",
)
