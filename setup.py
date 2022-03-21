from setuptools import setup, find_packages
from ouija_board import __version__

setup(
    name="ouijaboard",
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=["click==7.1.2", "colorzero==1.1", "Flask==1.1.2",
                      "gpiozero==1.5.1", "itsdangerous==1.1.0", "Jinja2==2.11.3",
                      "MarkupSafe==1.1.1", "Paste==3.4.3", "six==1.15.0", "waitress==2.1.1",
                      "Werkzeug==1.0.1"],

    author="Sam O'Keefe",
    author_email="sjo91190@gmail.com",
    description="Raspberry Pi Powered LED Ouija Board",
    url="https://github.com/sjo91190/led-ouija-board"
)
