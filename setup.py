from setuptools import setup, find_packages

requirements_file = './requirements.txt'

with open(requirements_file, 'r') as f:
    install_requires = [
        line for line in f.read().splitlines() if len(line) > 0]

setup(
    name='tictactoe',
    description='simple command line tictactoe game',
    author='sushant',
    author_email='sushant.padha@gmail.com',
    version='1.0',
    url='https://github.com/Sushant-Padha/tictactoe',
    license='MIT License',
    packages=find_packages(),
    install_requires=install_requires
)
