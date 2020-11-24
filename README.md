# python-cli-poc

A proof of concept of creating a python based cli to automate tasks based on a manifest.yaml.

## Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

``` bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- or use the [poetry](https://python-poetry.org/docs/) tool for dependency management and packaging in Python.

``` bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry shell
poetry install
```

## Click CLI Example

- Our initial CLI reads a CSV file from disk, processes it and stores the result in an Excel file.
- The path to the input and the output file should be configurable by the user.
- The user must specify the input file path.
- Specifying the output file path is optional and defaults to output.xlsx.

``` python

import click
@click.command()
@click.option("--in", "-i", "in_file", required=True,
    help="Path to csv file to be processed.",
)
@click.option("--out-file", "-o", default="./output.xlsx",
    help="Path to excel file to store the result.")
def process(in_file, out_file):
    """ Processes the input file IN and stores the result to
    output file OUT.
    """
    input = read_csv(in_file)
    output = process_csv(input)
    write_excel(output, out_file)
if __name__ =="__main__":
    process()

```

## Usage

``` bash
# activate the virtualenv
poetry shell
# Prints help
python3 -m cli_tutorial.cli --help
# Use single char -i for loading the file
python3 -m cli_tutorial.cli -i dummy.csv
# Specify both file with long name
python3 -m cli_tutorial.cli --in dummy.csv --out-file out.xlsx
```

## Running Tests

``` bash

poetry run pytest

```

## References

- [How to Write Python Command-Line Interfaces like a Pro](https://towardsdatascience.com/how-to-write-python-command-line-interfaces-like-a-pro-f782450caf0d)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you **would** like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
