from cleaner import clean_company_name
import logging
from loader import load_companies_csv
from json_output import output_json
from fetch_website import fetch_website
from url_utilities import normalize_url
from clean_data import clean_text, normalize_company_name
from is_website_duplicate import is_website_duplicate

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    
    datefmt="%Y-%m-%d %H:%M",
)

logging.info("The worker started")

#Load company data from CSV file
companies = load_companies_csv("companies.csv")

companies_data = []

#Log companies that have a valid website, log errors and create companies_data dictionary
for i in range(len(companies)):
    try:
        company_website = normalize_url(companies[i]["website"])
        company_name = normalize_company_name(companies[i]["company_name"])

        if company_website and not is_website_duplicate(companies_data, company_website):
            companies_data.append({"company_name": company_name, "company_website": company_website})
            logging.info(f"{clean_company_name(company_name)} was processed")
        else:
            logging.warning(f"{companies[i]} was skipped")

    except (ValueError, IndexError, TypeError, IndexError) as e:
        logging.error(f"%s caused an error at index {i}", companies[i])

#add wesite text to companies_data
for company in companies_data:
    company["website_content"] = fetch_website(company["company_website"])

#convert the dictionary to a json object and write it into JSON file
output_json("output-data.json", companies_data)

logging.info("The worker finished")