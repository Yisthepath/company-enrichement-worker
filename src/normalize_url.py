from urllib.parse import urlparse, urlunparse
from normalize_domain import normalize_domain
from is_path_useful import is_path_useful
from remove_tracking_queries import remove_tracking_queries


def normalize_url(url):
    """
    normalizes a given url

    Args:
        -url (str | None): the website's URL

    Returns:
        - normalized_url (str | None): the websites normalized URL
    """
    if url == None or url.strip() == "":
        return None

    url = url.strip().lower()

    if not (url.startswith("https://") or url.startswith("http://")):
        url = "https://" + url

    parsed = urlparse(url)
    scheme = parsed.scheme.strip()
    domain = normalize_domain(parsed.netloc).strip()
    path = parsed.path.strip()

    if path.endswith("/"):
        path = path[: len(path) - 1]

    parameters = ""
    queries = parsed.query.strip()
    fragment = ""

    if is_path_useful(path):
        path = path
    else:
        path = ""

    if is_path_useful(path):
        queries = remove_tracking_queries(queries)
    else:
        queries = ""

    normalized_url = urlunparse((scheme, domain, path, parameters, queries, fragment))

    return normalized_url
