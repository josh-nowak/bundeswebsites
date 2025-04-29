# Bundeswebsites

This project extracts data from German federal websites that were disclosed in February 2025 in a response to a [_Kleine Anfrage_](https://dserver.bundestag.de/btd/20/150/2015028.pdf). The dataset includes URLs, HTTP status codes, site titles, and meta descriptions.

## Usage

The file [`bundeswebsites.csv`](./bundeswebsites.csv) contains the generated dataset.

If you would like to build the dataset yourself, do the following:

- Make sure you have [uv](https://docs.astral.sh/uv/) installed
- Run `uv sync` to create the environment at `./.venv`
- Run the notebook `bundeswebsites.ipynb` with the environment created above (e.g., using the "Select Kernel" option in VS Code)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
