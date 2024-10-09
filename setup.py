from setuptools import setup, find_packages

setup(
    name="position-encoding",
    description="A library that encodes sequence positions in torch",
    version="1.0.0",
    packages=find_packages("position_encoding"),
    install_requires = [
        "torch>=2.0.1",
    ],
)
