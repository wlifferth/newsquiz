# Headline Project

## Project Overview

This project is designed to scrape news headlines from RSS feeds, process them, and then generate questions based on these headlines. It identifies named entities within the headlines to create multiple-choice questions, selecting one entity as the correct answer and finding semantically similar but distinct entities as distractors.

## Features

*   **RSS Scraping:** Fetches articles from RSS feeds (e.g., New York Times).
*   **Headline Parsing:** Extracts relevant information from scraped articles.
*   **Cloud Storage:** Supports writing parsed headline data to Google Cloud Firestore.
*   **Question Generation (QGen):**
    *   Named Entity Recognition (NER).
    *   Selection of a target named entity as the "answer".
    *   Generation of plausible alternate answers (distractors) based on semantic similarity and distinct identity.

## Project Structure

The project is organized into the following main directories:

*   `QGen/`: Contains the logic for question generation. See `QGen/README.md` for more details.
*   `scraping/`: Contains scripts and modules for fetching and parsing articles from RSS feeds.
    *   `scraping/parsers/`: Includes specific parsers for different news sources (e.g., `nyt_parser.py`).
*   `test/`: Contains unit tests for the project (e.g., `TestFingerprint.py`).

## Setup and Installation

1.  **Google Cloud Credentials:**
    If you intend to use Google Cloud Firestore for storing scraped data, you need to set up authentication.
    *   Ensure you have the `gcloud` CLI tool installed and configured.
    *   Run the `get_credentials.sh` script:
        ```bash
        sh get_credentials.sh
        ```
    *   This script will create a `credentials.json` file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

2.  **Python Dependencies:**
    The project uses Python and has a list of dependencies specified in `requirements.txt`.
    *   It is recommended to use a virtual environment.
    *   Install the dependencies using pip:
        ```bash
        pip install -r requirements.txt
        ```

## How to Run

### Scraping Headlines

The `scraping/scrape.py` script is used to fetch and process headlines.

*   **Basic Usage (scrape from NYT RSS feed and print to stdout):**
    ```bash
    python scraping/scrape.py
    ```

*   **Scraping from a local file (e.g., for testing):**
    ```bash
    python scraping/scrape.py --source_type file --source_file_path /path/to/your/rss_feed.xml
    ```

*   **Writing to Google Cloud Firestore:**
    ```bash
    python scraping/scrape.py --write_to cloud
    ```
    (Ensure you have completed the credential setup above).

*   **Other options:**
    Use the `--help` flag to see all available command-line arguments:
    ```bash
    python scraping/scrape.py --help
    ```

### Running Tests

To run the unit tests, navigate to the project's root directory and use the Python `unittest` module:

```bash
python -m unittest discover
```

## QGen Module

The `QGen` module is responsible for generating questions from the processed headlines. It involves complex logic for named entity handling and selecting appropriate distractors. For a more detailed explanation of its functionality and challenges, please refer to the `QGen/README.md` file.
