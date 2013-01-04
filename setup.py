import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="skinner",
    version="1.0",
    author="Joshua Goodlett",
    author_email="joshuagoodlett@gmail.com",
    url="https://github.com/jgoodlet/skinner",
    description="A Python static site generator.",
    install_requires="",
    entry_points={
        "console_scripts": ["skinner = skinner.cli.main"]
    }
)