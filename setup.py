from setuptools import setup, find_packages

__version__ = "1.1.0"

setup(
    name="ouijaboard",
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=["Flask==1.1.2", "SQLAlchemy==1.4.3", "SQLAlchemy==1.4.3",
                      "gpiozero==1.5.1", "Paste==3.4.3", "waitress==1.4.4", "RPi.GPIO==0.7.0"],

    author="Sam O'Keefe",
    author_email="sjo91190@gmail.com",
    description="Raspberry Pi Powered LED Ouija Board",
    url="https://github.com/sjo91190/led-ouija-board"
)
