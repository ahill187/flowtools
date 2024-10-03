from setuptools import setup

setup(
    name="flowtools",
    version="0.0.1",
    description="Flow Cytometry Tools",
    author="Ainsleigh Hill",
    author_email="ainsleighhill@gmail.com",
    packages=["flowtools"],
    install_requires=[
      line.strip() for line in open("requirements.txt")
    ],
    extras_require={
        "dev": [line.strip() for line in open("requirements-dev.txt")],
        "docs": [line.strip() for line in open("requirements-docs.txt")]
    }
)