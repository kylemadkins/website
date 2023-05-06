import re

def strip_tags_from_body(body: str) -> str:
    html = str(body)
    without_code_blocks = re.sub("<pre>((.|\n)*?)</pre>", "", html)
    without_tags = re.sub("<[^<]+?>", "", without_code_blocks)
    return without_tags.strip()
