from bs4 import BeautifulSoup
from url_utilities import make_absolute_url
from is_url_useful import is_url_useful
from is_duplicate_link import is_duplicate_link
from clean_data import clean_text, deduplicate_list
import re
from email_extractor import email_extractor

def parse_html(html, url):
    """
    parses through html code with and returns the title and description

    Args:
        -html (str): html code to be parsed through
        - url (str): the url of the source page

    Returns:
        - parsed_dict: a dicttionary containing the following data
            - "title" (str | None): the page's title
            - "description" (str | None): the page's description
            - "headers" (list | None): the page's headers
            - "links" (list | None)": the page's useful links
    """

    parsed_dict = {}
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    description_tag = soup.find("meta", attrs= {"name": "description"})
    description_og_tag = soup.find("meta", attrs= {"property": "og:description"})
    header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    a_tags = soup.find_all("a")

    page_headers = []
    page_links = []

    if title_tag != None:
        page_title = title_tag
        page_title = clean_text(str(page_title.get_text(strip=True)))
    else:
        page_title = None

    if description_tag!= None:
        page_description = description_tag
        page_description = clean_text(str(page_description.get("content")).strip())
    elif description_og_tag:
        page_description = description_og_tag
        page_description = clean_text(str(page_description.get("content")).strip())
    else:
        page_description = None
    
    if list(header_tags) != []:
        for tag in header_tags:
            page_headers.append(str(tag.get_text(strip=True)))
    else:
        page_headers = None

    page_headers = deduplicate_list(page_headers)

    if a_tags != []:
        for tag in a_tags:
            href = str(tag.get("href"))
            href = make_absolute_url(url, href)

            if href and is_url_useful(href) and not is_duplicate_link(page_links, href):
                page_links.append(
                {
                    "text": str(tag.get_text(strip=True)), 
                    "link": href
                })
            else:
                href = None
    else:
        page_links = None

    parsed_dict["title"] = page_title
    parsed_dict["description"] = page_description
    parsed_dict["headers"] = page_headers
    parsed_dict["links"] = page_links

    public_emails = email_extractor(parsed_dict["links"])

    parsed_dict["public_emails"] = public_emails

    return parsed_dict