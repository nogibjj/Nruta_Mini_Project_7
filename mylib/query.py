"""Query the database"""

from dotenv import load_dotenv
from databricks import sql
import os

complex_query = """SELECT d.title, AVG(d.year_release) AS year_released, 
s.number_of_subjects, s.subject
FROM default.nmc_biopics_details AS d
JOIN default.nmc_biopics_subjects AS s ON d.title = s.title
GROUP BY d.title, s.number_of_subjects, s.subject
ORDER BY d.title ASC;
"""


def run_query():
    load_dotenv()

    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                WITH joined_biopics AS (
                    SELECT b.title, b.country, b.year_release, 
                    b.box_office, s.subject, s.subject_race, s.subject_sex
                    FROM nmc_biopics_details b
                    JOIN nmc_biopics_subjects s
                    ON b.title = s.title
                )
                SELECT * FROM joined_biopics;
            """
            )

            result = cursor.fetchall()
            for row in result:
                print(row)

        cursor.close()
    return "Query successful."


def filter_by_year(year):
    load_dotenv()

    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            # Use f-string to insert year directly into the SQL query
            query = f"""
                SELECT DISTINCT b.title, b.year_release, s.subject
                FROM nmc_biopics_details b
                JOIN nmc_biopics_subjects s ON b.title = s.title
                WHERE b.year_release = {year}
            """
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        cursor.close()
    return "Filter by year successful."


if __name__ == "__main__":
    run_query()
    filter_by_year()
