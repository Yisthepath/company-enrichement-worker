import requests
import logging

logging.basicConfig(
    force=True,
    level=logging.DEBUG,
    filename="requests.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

from parser import parse_html


def fetch_website(url):
    """
    fetches a website and returns its homepage's title and descrition

    Args:
        -url (str): the website's URL

    Returns:
        - dict: a dicttionary containing the following data
            - "title" (str | None): the page's title
            - "description" (str | None): the page's description
            - headers (str | None): the page's headers
            - useful links (str | None): useful links found in the page
    """

    header = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }
    try:
        result = requests.get(url, headers=header, timeout=10)
        result.raise_for_status()
        logging.info(f"fetching {url} suceeded")
        return parse_html(result.text, url)

    except requests.exceptions.HTTPError as e:
        logging.error(
            f"fetching {url} resulted in the following error: {e} (status code: {result.status_code})"
        )
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.SSLError,
        requests.exceptions.MissingSchema,
        requests.exceptions.InvalidURL,
    ) as e:
        logging.error(f"fetching {url} resulted in the following error: {e}")
    except requests.exceptions.Timeout as e:
        logging.warning(f"{url} timed out")
