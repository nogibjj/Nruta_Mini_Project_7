[![CI](https://github.com/nogibjj/Nruta_Mini_Project_7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_7/actions/workflows/cicd.yml)

# IDS 706 Week 7 Mini Project - Packaging a Python Script into a Command-Line Tool (or Rust)

## 🏗️ Requirements
- Package a Python script with setuptools or a similar tool
- Include a user guide on how to install and use the tool
- Include communication with an external or internal database (NoSQL, SQL, etc)

## 📂 Project Structure
```
.
├── Makefile
├── README.md
├── data
│   └── biopics.csv
├── main.py
├── mylib
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── requirements.txt
├── setup.sh
└── test_main.py
```

## 📦 Files and Directories
- extract.py: Extracts raw data from the source.
- load.py: Loads processed data into tables.
- query.py: Executes complex SQL queries (self-joins, joins).
- test_main.py: Unit tests for project functions.

## 🛠️ Setup Instructions
1. Clone the repository:
```
git clone https://github.com/nogibjj/Nruta_Mini_Project_6
```

2. Navigate to the project directory:
```
cd Nruta_Mini_Project_6
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## 📊 Dataset Description
The data for this project comes from the `biopics.csv` dataset provided by FiveThirtyEight. After importing the dataset, I split it into two tables to organize the information more effectively:

- `nmc_biopics_details`: This table contains core information about each biopic, such as the title, release year, and other relevant attributes.
- `nmc_biopics_subjects`: This table includes details about the subjects or individuals the biopics are based on, including the number of subjects featured and their respective roles.

## 🗃️ Complex SQL Query
Once the data was split, I constructed the following query to analyze the average release year of the biopics alongside the subjects they feature:

```
SELECT 
    d.title, 
    AVG(d.year_release) AS year_released, 
    s.number_of_subjects, 
    s.subject
FROM default.nmc_biopics_details AS d
JOIN default.nmc_biopics_subjects AS s 
    ON d.title = s.title
GROUP BY 
    d.title, 
    s.number_of_subjects, 
    s.subject
ORDER BY d.title ASC;
```

Explanation:
- `SELECT`: Retrieves the title of each biopic, the average release year (year_released), the number of subjects, and the subjects' names.
- `JOIN`: Combines the nmc_biopics_details and nmc_biopics_subjects tables based on the biopic title.
- `GROUP BY`: Groups the results by biopic title, number of subjects, and the subjects themselves to ensure we get accurate averages and associations.
- `ORDER BY`: Sorts the output in ascending order by the biopic title for easier readability.

## 💻 CLI Setup

This project includes a command-line interface (CLI) for easy interaction with the application.

### File Descriptions
- **`setup.py`**: Packaging script for easy installation.
- **`cli_tool.py`**: Main module for defining CLI commands.
- **`biopics-cli`**: Command-line script for user interaction.

### Installation Instructions
Run the following command in the terminal:

```
pip install .
```

### Year Query

The Year Query feature allows users to filter biopic data by the release year. This functionality can be particularly useful for analyzing trends in biopics over different periods. 

#### Usage

To execute a year query, run the following command:

```
python cli_tool.py --year <YEAR>
```

## 🎯 Complex Query Expected Output
After running the SQL query, the output is as follows:
<img width="990" alt="Screenshot 2024-10-18 at 17 22 12" src="https://github.com/user-attachments/assets/7a4959f4-840b-47d4-af08-f7c234d0595d">

## 📃 CLI Expected Output
After running the Year Query, the expected output will be a list of biopics filtered by the specified release year. Here’s an example of what the output might look like:

