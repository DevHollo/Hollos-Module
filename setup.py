from setuptools import setup

with open('README.md', 'r') as mdfile:
    des = mdfile.read()

setup(
    name='Hollos-Module',
    version='0.0.3',
    scripts=['hollosmodule.py'],
    author="Hollo",
    author_email="hollo1234567890e@gmail.com",
    long_description=des,
    long_description_content_type="text/markdown",
    install_requires=[
        "sty==1.0.6",
        "requests==2.31.0",
        "getpass4==0.0.14.1",
        "pillow==10.2.0",
        "qrcode==7.4.2"
    ],
    url="https://github.com/DevHollo/Hollos-Module"
)
