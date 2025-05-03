# Bundeswebsites

## Overview

This project compiles a comprehensive dataset of German federal websites that were disclosed in February 2025 in response to a [_Kleine Anfrage_](https://dserver.bundestag.de/btd/20/150/2015028.pdf) to the German parliament. The dataset includes both active and deprecated websites from various German federal government departments.

## Dataset Contents

The source data contains URLs and their associated government departments ("Ressorts"). The dataset is then enriched with additional information.

- **ressort**: Government department responsible for the website
- **url**: Website URL
- **title**: Website title (from HTML title tag)
- **description**: Website description (from meta description tag)
- **initial_status**: HTTP status code at the time of query before following redirects
- **final_status**: HTTP status code at the time of query after following redirects
- **hreflang**: Alternative language versions of the website (from alternate link tags)
- **canonical_url**: Canonical URL of the website (from canonical link tag)
- **uses_gsb**: Indicates whether the website was created with the Government Site Builder (from generator tag)

## Installation

### Prerequisites

- [uv](https://docs.astral.sh/uv/) package manager
- Python 3.12+
- Jupyter notebook environment (e.g., VS Code with Jupyter extension)

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/josh-nowak/bundeswebsites.git
   cd bundeswebsites
   ```

2. Create and activate the virtual environment:
   ```bash
   uv sync
   ```
   This will create the environment in `./.venv`

## Usage

### Pre-built Dataset

The file [`bundeswebsites.csv`](./bundeswebsites.csv) contains the complete generated dataset ready for use.

### Building the Dataset

If you want to generate the dataset yourself:

1. Ensure you have set up the environment as described above
2. Open and run the Jupyter notebook. For example, in VS Code, open the notebook and select the kernel from the `./.venv` environment

## Contributing

Contributions are welcome. Feel free to open a pull request.
