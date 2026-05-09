def is_duplicate_link(items, link):
    """
    determines if a link already appears in a items

    -Args:
        - items (list): the list containing links
        - link (str) : the link to be checked

    -Returns:
        - is_duplicate (boolean): returns True if link is a duplicate and False otherwise
    """

    if not items:
        return False

    is_duplicate = False

    for e in items:
        if e["link"] == link:
            is_duplicate = True
            break

    return is_duplicate
