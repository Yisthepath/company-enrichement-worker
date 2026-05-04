from bs4 import BeautifulSoup

def parse_html(html):
    """
    parses through html code with and returns the title and description

    Args:
        -html (str): html code to be parsed through

    Returns:
        - dict: a dicttionary containing the following data
            - "title" (str | None): the page's title
            - "description" (str | None): the page's description
    """

    parsed_dict = {}
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    description_tag = soup.find("meta", attrs= {"name": "description"})
    description_og_tag = soup.find("meta", attrs= {"property": "og:description"})

    if title_tag != None:
        page_title = title_tag
        page_title = str(page_title.get_text(strip=True))
    else:
        page_title = None
    if description_tag!= None:
        page_description = description_tag
        page_description = str(page_description.get("content")).strip()
    elif description_og_tag:
        page_description = description_og_tag
        page_description = str(page_description.get("content")).strip()
    else:
        page_description = None
    
    parsed_dict["title"] = page_title
    parsed_dict["description"] = page_description

    return parsed_dict