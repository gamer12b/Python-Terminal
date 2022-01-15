import setuptools
from setuptools import find_packages
from setuptools import setup
import platform

if platform.system().lower() == "windows":
    setup(
        name="terminal",
        version="1.0.0",
        description="This a simple python terminal",
        author="William Johansson",
        author_email="will04459@gmail.com",
        url="https://github.com/gamer12b/Python-Terminal",
        packages=find_packages(),
        install_requires=["wget","js2py","psutil","pytube"],
        keywords=["python","terminal","cli","terminal-cli","python-cli","cmd","email","pytube"]
    )
else:
    print("This does currently does not support linux, but its coming later´or you can modify it yourself.")