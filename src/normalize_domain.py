def normalize_domain(domain):
    """
    normalize a given domain
    example: www.example.org becomes https://example.org

    Args:
        -domain (str): a url's domain

    Returns:
        - domain (str): a normalized version of the given domain
    """

    if domain.startswith("www."):
        domain = domain[4:]

    return domain
