# tictactoe

simple command line tictactoe game

## Installation

1. Download the source code.
2. Open up a terminal.
3. `cd` into the project root†.
4. Run the command (mind the period at the end of the command)

   ```bash
   python -m pip install -e .
   ```

## Usage

Follow the steps outlined in the [Installation](#installation) section.

Play the game with the command

```bash
python tictactoe
```

## Developing

Follow the steps outlined in the [Installation](#installation) section.

To develop you will need to install [Python3](https://python.org) for your specific OS and architecture

Other than that, you will also need the following dependencies:

- [pytest](https://pytest.org) (v6.2.1) for running tests
- [pycodestyle](https://pypi.org/project/pycodestyle/) (v2.6.0) for linting
- [autopep8](https://pypi.org/project/autopep8/) (v1.5.4) for formatting

They can be installed from the `requirements.txt` file provided in the source.

Just run

```bash
python -m pip install -r requirements.txt
```

Preferable, you should use [git](https://git-scm.com) for version control and [virtual environments](https://docs.python.org/3/tutorial/venv.html) for creating a reusable, isolated environment

The project is installed in [editable](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) state, so you can start developing straight away.

To run tests, simply `cd` into the source root†† and execute the following command

```bash
python -m pytest .
```

It is preferred to use the [Visual Studio Code](https://code.visualstudio.com) editor for this project because of its useful extensions and features for python, smooth integration with various formatters, linters and other services and user friendly interface.

For new contributors, these links may be useful for understanding more about the tools used:

* [Getting Started with Python](https://www.python.org/about/gettingstarted)
* [Hello World for Git](https://guides.github.com/activities/hello-world/)
* [Start using Git on the command line](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
* [Python virtual environments](https://docs.python.org/3/tutorial/venv.html)
* [A Guide To Python's Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)
* [Using pytest](https://docs.pytest.org)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Todo

- [ ] Add an AI to play against player

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

† Project root is the folder named "tictactoe" at the top level, i.e., it is shallow

†† Source root is the folder named "tictactoe" inside another folder named "tictactoe", i.e., it is deep (nested)
