from setuptools import setup, find_packages

setup(
    name="ouijaboard",
    version="0.1",
    packages=find_packages(),
    install_requires=["click==7.1.2"
                      "colorzero==1.1",
                      "Flask==1.1.2",
                      "gpiozero==1.5.1",
                      "itsdangerous==1.1.0",
                      "Jinja2==2.11.2",
                      "MarkupSafe==1.1.1",
                      "Paste==3.4.3",
                      "six==1.15.0",
                      "waitress==1.4.4",
                      "Werkzeug==1.0.1"],


    # metadata to display on PyPI
    author="Sam O'Keefe",
    author_email="sjo91190@gmail.com",
    description="Raspberry Pi Powered LED Ouija Board",
    url="https://github.com/sjo91190/led-ouija-board"
)
