from urllib.parse import urlparse, parse_qsl
def is_url_useful(url):
    """
    determines if a url is likely useful for the purposes of this project

    Args:
        -url (str): the input url

    Returns:
        - is_useful (boolean): True if the url is useful False otherwise
    """
       
    parsed = urlparse(url)
    path = parsed.path

    if not path or path.strip() == "":
        return False

    is_useful = False

    useful_paths = {
        # 1. About / company identity pages
        "/about",
        "/about-us",
        "/company",
        "/who-we-are",
        "/our-story",
        "/story",
        "/mission",
        "/vision",
        "/values",
        "/what-we-do",
        "/page",
        "/search",

        # 2. Careers / hiring pages
        "/careers",
        "/jobs",
        "/join-us",
        "/join",
        "/work-with-us",
        "/open-roles",
        "/openings",
        "/career",
        "/opportunities",
        "/talent",
        "/life-at-company",

        # 3. Team / leadership pages
        "/team",
        "/our-team",
        "/leadership",
        "/management",
        "/executive-team",
        "/founders",
        "/people",
        "/board",
        "/advisors",

        # 4. Contact pages
        "/contact",
        "/contact-us",
        "/get-in-touch",
        "/talk-to-us",
        "/connect",
        "/support/contact",
        "/company/contact",

        # 5. Product pages
        "/product",
        "/products",
        "/platform",
        "/solution",
        "/solutions",
        "/software",
        "/services",
        "/features",
        "/use-cases",
        "/how-it-works",

        # 6. Solutions / customer segment pages
        "/solutions/enterprise",
        "/solutions/small-business",
        "/solutions/startups",
        "/solutions/agencies",
        "/solutions/sales",
        "/solutions/marketing",
        "/solutions/hr",
        "/industries",
        "/industries/finance",
        "/industries/healthcare",
        "/industries/retail",
        "/customers",

        # 7. Funding / investor / press-release pages
        "/news",
        "/press",
        "/press-releases",
        "/newsroom",
        "/media",
        "/investors",
        "/investor-relations",
        "/company-news",
        "/announcements",
        "/blog",
    }

    for useful_path in useful_paths:
        if path.startswith(useful_path):
            is_useful = True
            break

    return is_useful