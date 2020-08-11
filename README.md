This project is written in Python and uses [poetry](https://python-poetry.org/) to manage dependencies.

To install dependencies:

    poetry install

To run the script against a log file:

    poetry run python log_monitor/log_monitor.py < logfile

To run unit tests:

    poetry run pytest
