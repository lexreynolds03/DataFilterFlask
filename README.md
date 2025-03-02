# CSV Data Filter Flask Application

This is a simple Flask web application that reads computer part data from a CSV file and allows users to filter the data based on the part's name, type, and brand. The app will display the filtered results in real-time based on the user's input.

## Features

- Reads data from a CSV file (`data.csv`).
- Filters data by part name, type, and brand using a web form.
- Real-time filtering with no page reloads required.
- Handles BOM (Byte Order Mark) characters from the CSV file for clean data input.

## Requirements

- Python 3.x
- Flask
- CSV file with columns like `Name`, `Type`, and `Brand`.

## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required dependencies by running:

```bash
pip install flask
