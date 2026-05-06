def is_website_duplicate(items, website):
    """
    determines if a website is a duplicate

    -Args:
        - items (list): the list containing websites
        - website (str) : the website to be checked
    
    -Returns:
        - is_duplicate (boolean): returns True if link is a duplicate and False otherwise
    """

    if not items:
        return False
    
    is_duplicate = False

    for e in items:
        if e["company_website"] == website:
            is_duplicate = True
            break
    
    return is_duplicate