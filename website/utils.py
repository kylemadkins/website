import re

def strip_tags_from_body(body: str) -> str:
    html = str(body)
    without_tags = re.sub("<[^<]+?>", "", html)
    without_newlines = re.sub("[\n\r]", "", without_tags)
    return [word for word in without_newlines.strip().split(" ") if word != ""]
