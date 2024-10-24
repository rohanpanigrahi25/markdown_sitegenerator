def extract_title(markdown):
    if len(markdown) != 0:
        if markdown.startswith('# '):
            title = markdown.lstrip('#').strip()
            return title
        else:
            raise Exception("No h1 header in the given markdown")
    else:
        raise Exception("Markdown is empty")
    