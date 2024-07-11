# Data Extractor

## Overview

Data Extractor is a tool designed to receive a question in English as input and return an Excel file containing the requested information extracted from a dataset. It utilizes OpenAI's language model to interpret the question and extract relevant data from a provided `.csv` file.

## Example

**Input:**
What was the total credit amount last month?

**Output:**
Returns an Excel file with the total credit amount from the last month.

## Features

- **Automated Data Extraction**: Automatically extracts data from a `.numbers` file.
- **Natural Language Query**: Interprets questions asked in English.
- **Excel Output**: Provides the response in a neatly formatted Excel file.
- **Modular Design**: Easy to extend and maintain.

## Setup

### Prerequisites

- Python 3.11.9
- An OpenAI API key

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/YigitKeser/Data-Extractor.git
    ```

2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure the `config.ini` file**:
   Update `config.ini` with your OpenAI API key and file paths.
    ```ini
    [OPENAI]
    OPENAI_API_KEY = your_openai_api_key

    [PATH]
    INPUT_FILE = data/credit_data.numbers
    OUTPUT_FILE = output/response.xlsx
    ```
### Usage

Run the tool with your query:
```sh
python main.py
```
