# Advent of Code Offline

A Python script to download all problem sets and input files from [Advent of Code](https://adventofcode.com). Useful if you wanna go offline or just want to keep a local copy of the problems.

## Features

- Downloads problem sets (`index.html`) for each day.
- Downloads input files (`input.txt`) for each day.
- Organizes files into `{year}/day/{day_number}` directories.

## Requirements

- Python 3.7 or higher
- `requests` library (see [requirements.txt](requirements.txt))

## Installation

1. Clone this repository or download the script.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

Run the script with your Advent of Code session token:

python script.py <year> --start_day <start_day> --end_day <end_day> --session_token <session_token>
```
<year>: Year of the Advent of Code (e.g., 2021).
--start_day: Starting day (default: 1).
--end_day: Ending day (default: 25).
--session_token: Your session token from Advent of Code cookies.
```

### Example

``python script.py 2022 --session_token YOUR_SESSION_TOKEN``

This will download all problems and inputs for 2022.

## Notes

- Your session token is required to access the input files.
- Ensure your session token is kept private and not shared.

## License

MIT License
