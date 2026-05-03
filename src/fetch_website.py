import requests
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="requests.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    
    datefmt="%Y-%m-%d %H:%M",
)

def fetch_website(url):
    header = {"User-Agent": "Mozilla/5.0"}
    try:
        result = requests.get(
            url, 
            headers=header,
            timeout=10)
        result.raise_for_status()
        logging.info(f"fetching {url} suceeded")
        return result.text

    except requests.exceptions.HTTPError as e:
        logging.error(f"fetching {url} resulted in the following error: {e} (status code: {result.status_code})")
    except (requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects, requests.exceptions.SSLError, requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as e:
        logging.error(f"fetching {url} resulted in the following error: {e}")
    except requests.exceptions.Timeout as e:
        logging.warning(f"{url} timed out")