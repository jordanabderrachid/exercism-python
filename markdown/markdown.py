import re


def parse(markdown):
    lines = markdown.split("\n")
    res = ""
    in_list = False
    in_list_append = False
    for line in lines:
        line = apply_heading_tag(line)

        m = re.match(r"\* (.*)", line)
        if m:
            curr = m.group(1)
            line = "<li>" + curr + "</li>"
            if not in_list:
                in_list = True
                line = "<ul>" + line
        else:
            if in_list:
                in_list_append = True
                in_list = False

        line = apply_paragraph_tag(line)
        line = apply_strong_tag(line)
        line = apply_em_tag(line)

        if in_list_append:
            line = "</ul>" + line
            in_list_append = False
        res += line
    if in_list:
        res += "</ul>"
    return res


def apply_heading_tag(line: str) -> str:
    pattern = "(#{1,6}) (.*)"
    match = re.match(pattern, line)
    if match is None:
        return line

    level = len(match.group(1))
    return "".join([f"<h{level}>", match.group(2), f"</h{level}>"])


def apply_strong_tag(line: str) -> str:
    return apply_emphasis(line, 2, "strong")


def apply_em_tag(line: str) -> str:
    return apply_emphasis(line, 1, "em")


def apply_emphasis(line: str, underscore_count: int, tag: str) -> str:
    pattern = (
        "(.*)" + ("_" * underscore_count) + "(.*)" + ("_" * underscore_count) + "(.*)"
    )
    m = re.match(pattern, line)
    if m is None:
        return line

    return m.group(1) + f"<{tag}>" + m.group(2) + f"</{tag}>" + m.group(3)


def apply_paragraph_tag(line: str) -> str:
    m = re.match("<h|<ul|<p|<li", line)
    if not m:
        line = "<p>" + line + "</p>"

    return line
