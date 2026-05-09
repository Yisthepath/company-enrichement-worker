from urllib.parse import parse_qsl, urlencode


def remove_tracking_queries(queries):
    """
    removes tracking queries from a url's queries

    Args:
        - queries (str): a url's queries
    Returns:
        - cleaned_queries (list): a cleaned version of the queries
    """

    query_pairs = parse_qsl(queries)

    tracking_queries = {
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

    cleaned_query_pairs = []

    for key, value in query_pairs:
        if key.lower() not in tracking_queries:
            cleaned_query_pairs.append((key, value))

    cleaned_queries = urlencode(cleaned_query_pairs)

    return cleaned_queries
