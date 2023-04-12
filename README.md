# poetry-playground

📚 Learning and exploring Poetry, the Python package manager.

> Python packaging and dependency management made easy.
> 
> -- <cite>https://python-poetry.org</cite>

**NOTE**: This project was developed on macOS and for my own personal use.


## Overview

This repository is for me to learn Poetry and have working example code/configuration that I look back on in my future
development in the Python ecosystem. Personally, I like to use JetBrains IDEs, and I'm using PyCharm for this project.
PyCharm has built-in support for Poetry. Let's explore it.


## Instructions

Follow these instructions to build and run the example project.

1. Pre-requisite: `poetry`
   * I'm using Python 3.11.3 and installed `poetry` 1.4.2 via `npx`
2. Run the example program
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

* I gather that pipx is probably a good choice? I haven't figured out if I need/want virtual environments.
* Stick with `python3` and `pip3` because `python` and `pip` are for macOS-provided distributions. Those are old.
* `pip3 install --user pipx`
* `pipx install poetry`
* `poetry completions bash > ${XDG_DATA_HOME:-~/.local/share}/bash-completion/completions/poetry`
* `poetry init`


## Wish List

General clean ups, TODOs and things I wish to implement for this project:

* [x] DONE Do a small "hello world" thing using a library.
   * I want to do a word count of my README.md into a Pandas DataFrame.
* [ ] What does packaging look like?
* [x] DONE Use the `__main__.py` pattern so that we can run the project with `-m` instead of pointing to a file.


## Reference

* [Poetry official docs](https://python-poetry.org/docs/)
  * > Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your
    > project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable
    > installs, and can build your project for distribution.  