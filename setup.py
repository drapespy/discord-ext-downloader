from setuptools import setup, find_packages
import re



version = '0.0.1-a'


setup(name='discord-ext-downloader',
    author='drapes',
    url='https://github.com/drapespy/discord-ext-downloader',
    version=version,
    packages=['discord.ext.downloader'],
    license='MIT',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description='An extension module to download YouTube videos',
    install_requires=['discord.py>=1.2.5'],
    python_requires='>=3.5.3'
)