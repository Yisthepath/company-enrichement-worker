import csv
from cleaner import clean_company_name


def load_companies_csv(file):
    with open(file, "r") as file:
        companies_csv = csv.DictReader(file)
        companies_list = []

        for row in companies_csv:
            companies_list.append(row)

        return companies_list
