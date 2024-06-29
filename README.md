# poetry-playground

📚 Learning and exploring Poetry, the Python package manager.

> Python packaging and dependency management made easy.
> 
> -- <cite>https://python-poetry.org</cite>

**NOTE**: This project was developed on macOS. It is designed for my own personal use.


## Overview

This repository is for me to learn Poetry and have working example code and configuration that I can look back on in my
future development in the Python ecosystem. Personally, I like to use JetBrains IDEs, and I'm using PyCharm for this
project. PyCharm has built-in support for Poetry. Let's explore Poetry.


## Instructions

Follow these instructions to build and run the example project.

1. Pre-requisite: Poetry
   * I'm using Poetry `1.8.3` which I installed via `pipx`.
2. Pre-requisite: Python
   * I'm using Python `3.12.3` which is available on my PATH as `python3` and `python3.12`.
3. Create a virtual environment
   * ```shell
     poetry env use python3.12
     ```
   * This will create a virtual environment tied to the Python interpreter pointed to by `python3.12` executable (or
     symlink) in a global cache directory that Poetry manages. Use the following command to see details about the
     virtual environment you just created.
   * ```shell
     poetry env info
     ```
   * For me, the output shows that the Python interpreter is located at `/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/bin/python3.12`.
     Manually creating a virtual environment in this way is actually not necessary. The first time you run `poetry install`,
     Poetry will automatically search for and use a Python interpreter matching the version specified in `pyproject.toml`.
     If it finds one (I don't know the algorithm it uses, but I suppose it just looks for executables on the PATH named
     `python3.11`, `python3.12`, etc.) then it creates the virtual environment before running the rest of the command. 
4. Install dependencies
   * ```shell
     poetry install
     ```
5. Run the example program
   * ```shell
     poetry run python -m poetry_playground
     ```


## Notes

This is not the first time I've dipped my toes into developing in the Python ecosystem, but in some ways it has the
same energy as that because I have to re-learn the various tools: pip, pipx, virtual environments, Poetry, etc. The goal
is not to learn them all in-depth but the goal is to learn enough to be able to support a project that supports my
ability to go in-depth on Python development itself. In other words, I want to learn Pandas, NumPy, Jupyter, and I don't
want to learn so much about the build tools.

Below are some stream of consciousness notes:

* `brew install pipx`
* `pipx install argcomplete`
* (Nushell) `register-python-argcomplete pipx | save ~/.local/share/bash-completion/completions/pipx` 
* `pipx install poetry`
* (Nushell) `poetry completions bash | save ~/.local/share/bash-completion/completions/poetry`
* `poetry init`
* `poetry lock`


## Wish List

General clean-ups, TODOs and things I wish to implement for this project:

* [x] DONE Do a small "hello world" thing using a library.
   * I want to do a word count of my README.md into a Pandas DataFrame.
* [ ] What does packaging look like?
* [x] DONE Use the `__main__.py` pattern so that we can run the project with `-m` instead of pointing to a file.
* [x] DONE Explore how Poetry interfaces with virtual environment.


## Reference

* [Poetry official docs](https://python-poetry.org/docs/)
  * > Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your
    > project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable
    > installs, and can build your project for distribution.  
