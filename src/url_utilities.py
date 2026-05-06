from urllib.parse import urlparse, urlunparse, urljoin, parse_qsl, urlencode


TRACKING_QUERIES = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "msclkid",
}


IGNORED_LINK_PREFIXES = (
    "mailto:",
    "tel:",
    "javascript:",
    "ftp:",
    "#",
)


def normalize_domain(domain):
    """
    Normalizes a given domain.
    Example: www.example.org becomes example.org

    Args:
        domain (str): A URL domain/netloc.

    Returns:
        str: A normalized version of the domain.
    """

    if not domain:
        return ""

    domain = domain.strip().lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def remove_tracking_queries(queries):
    """
    Removes tracking query parameters from a URL query string.

    Args:
        queries (str): A URL query string.

    Returns:
        str: A cleaned query string.
    """

    query_pairs = parse_qsl(queries)

    cleaned_query_pairs = []

    for key, value in query_pairs:
        if key.lower() not in TRACKING_QUERIES:
            cleaned_query_pairs.append((key, value))

    return urlencode(cleaned_query_pairs)


def should_ignore_link(link):
    """
    Checks whether a link should be ignored.

    Args:
        link (str | None): A link extracted from a webpage.

    Returns:
        bool: True if the link should be ignored, False otherwise.
    """
    if isinstance(link, str):
        link = link.strip().lower()
    if not link:
        return True


    return link.startswith(IGNORED_LINK_PREFIXES)


def normalize_url(url):
    """
    Normalizes a given URL.

    Args:
        url (str | None): The URL to normalize.

    Returns:
        str | None: The normalized URL, or None if invalid/empty.
    """

    if url is None or url.strip() == "":
        return None

    url = url.strip()

    if should_ignore_link(url):
        return None

    if not (url.startswith("https://") or url.startswith("http://")):
        url = "https://" + url

    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        return None

    scheme = parsed.scheme.lower()
    domain = normalize_domain(parsed.netloc)

    if not domain:
        return None

    path = parsed.path.strip()

    if path.endswith("/"):
        path = path[:-1]

    parameters = parsed.params
    queries = remove_tracking_queries(parsed.query)
    fragment = ""

    normalized_url = urlunparse((
        scheme,
        domain,
        path,
        parameters,
        queries,
        fragment
    ))

    return normalized_url


def make_absolute_url(website, link):
    """
    Converts a possibly relative link into a normalized absolute URL.

    Args:
        website (str): The base website URL.
        link (str): The extracted link.

    Returns:
        str | None: A normalized absolute URL, or None if invalid.
    """

    if not website or not link:
        return None

    if should_ignore_link(link):
        return None

    website = normalize_url(website)

    if not website:
        return None

    absolute_url = urljoin(website, link.strip())

    return normalize_url(absolute_url)