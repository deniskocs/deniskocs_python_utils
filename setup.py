from setuptools import setup, find_packages

setup(
    name="deniskocs_python_utils",
    version="0.1",
    packages=find_packages(),
    author="Denis Chilik",
    author_email="deniskocs@gmail.com",
    description="Utility classes required for other projects",
    url="https://github.com/deniskocs/deniskocs_python_utils",
    install_requires=[
        "matplotlib",
    ],
)