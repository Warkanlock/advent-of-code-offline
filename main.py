import os
import requests
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("advent_of_code_downloader.log")
    ]
)

def download_problem_set(year, start_day, end_day, session_token):
    base_url = "https://adventofcode.com"
    headers = {
        "Cookie": f"session={session_token}"
    }

    for day in range(start_day, end_day + 1):
        day_folder = f"{year}/day/{day}"
        os.makedirs(day_folder, exist_ok=True)

        logging.info(f"Downloading problem set for Day {day} of {year}...")

        # Download problem set page
        problem_url = f"{base_url}/{year}/day/{day}"
        problem_response = requests.get(problem_url, headers=headers)
        if problem_response.status_code == 200:
            with open(f"{day_folder}/index.html", "w", encoding="utf-8") as f:
                f.write(problem_response.text)
            logging.info(f"Problem set for Day {day} downloaded successfully.")
        else:
            print(f"Failed to download problem set for Day {day}: {problem_response.status_code}")
            logging.error(f"Failed to download problem set for Day {day}: {problem_response.status_code}")

        # Download input file
        logging.info(f"Downloading input file for Day {day} of {year}...")
        input_url = f"{base_url}/{year}/day/{day}/input"
        input_response = requests.get(input_url, headers=headers)
        if input_response.status_code == 200:
            with open(f"{day_folder}/input.txt", "w", encoding="utf-8") as f:
                f.write(input_response.text)
            logging.info(f"Downloaded input file for Day {day} successfully.")
        else:
            print(f"Failed to download input file for Day {day}: {input_response.status_code}")
            logging.error(f"Failed to download input file for Day {day}: {input_response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Advent of Code problem sets and inputs.")
    parser.add_argument("year", type=int, help="Year of the Advent of Code event")
    parser.add_argument("--start_day", type=int, default=1, help="Start day (default: 1)")
    parser.add_argument("--end_day", type=int, default=25, help="End day (default: 25)")
    parser.add_argument("--session_token", type=str, required=True, help="Session token from your Advent of Code login")

    args = parser.parse_args()

    download_problem_set(args.year, args.start_day, args.end_day, args.session_token)
