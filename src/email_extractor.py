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

import re


def email_extractor(useful_links_list):
    """ "
    checks if a link is likely contains emails and if it does, it extracts the emails from that page

    - Args:
        -useful_links_list (list | none): a list containing a dict that has a "text" key and a "link" key

    - Returns:
        -emails (list): a list containing all the emails found in the contact page(s)
    """
    if not useful_links_list:
        return []

    emails = []
    likely_useful_pages = r"\b(contact|contact us|contacts|get in touch|talk to us|reach us|connect with us|support|customer support|help|help center|contact support|technical support|sales|contact sales|talk to sales|speak to sales|request demo|book a demo|schedule demo|media contacts|press contacts|careers|jobs|join us|join our team|work with us|open roles|open positions|who we are|team|our team|leadership|founders|people|legal|investor relations|offices|locations|where we are)\b"
    links_to_visit = []
    for e in useful_links_list:
        if re.search(likely_useful_pages, e["text"], flags=re.IGNORECASE):
            links_to_visit.append(e["link"])

    header = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }

    for link in links_to_visit:
        try:
            result = requests.get(link, headers=header, timeout=10)
            result.raise_for_status()
            logging.info(f"fetching {link} suceeded")

            emails_in_html = re.findall(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", result.text
            )

            if emails_in_html:
                for email in emails_in_html:
                    if email and email not in emails:
                        emails.append(email)

        except requests.exceptions.HTTPError as e:
            logging.error(
                f"fetching {link} resulted in the following error: {e} (status code: {result.status_code})"
            )
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.SSLError,
            requests.exceptions.MissingSchema,
            requests.exceptions.InvalidURL,
        ) as e:
            logging.error(f"fetching {link} resulted in the following error: {e}")
        except requests.exceptions.Timeout as e:
            logging.warning(f"{link} timed out")

    return emails


test_list = [
    {"text": "What is Shopify?", "link": "https://shopify.com/blog/what-is-shopify"},
    {"text": "Careers", "link": "https://shopify.com/careers"},
    {"text": "Investors", "link": "https://shopify.com/investors"},
    {"text": "Newsroom", "link": "https://shopify.com/news"},
    {"text": "Blog", "link": "https://shopify.com/blog"},
    {"text": "Guides", "link": "https://shopify.com/blog/topics/guides"},
    {"text": "", "link": "https://linkedin.com/company/shopify"},
]
