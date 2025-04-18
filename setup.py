from setuptools import setup, find_packages

setup(
    name="multi-agent-llm",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0',
        'requests>=2.26.0'
    ]
)
