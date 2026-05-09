def clean_text(text):
    if not text:
        return ""

    text_list = text.split()

    clean_text = " ".join(text_list)

    return clean_text


def deduplicate_list(items):
    unique_list = []
    seen = set()

    for e in items:
        e = clean_text(e)
        if e and e not in seen:
            seen.add(e)
            unique_list.append(e)
    return unique_list


def normalize_company_name(name):
    return clean_text(name)
