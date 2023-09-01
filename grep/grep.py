import re


def grep(pattern, flags, files):
    matches = []

    for file_name in files:
        with open(file_name) as f:
            for line_number, line in enumerate(f.readlines()):
                if match(line, pattern, flags):
                    matches.append((file_name, line_number + 1, line))

    return render(matches, flags, files)


def render(matches, flags, files):
    if flags.find("-l") != -1:
        return render_file_names(matches, files)

    append_line_number = False
    if flags.find("-n") != -1:
        append_line_number = True

    append_file_name = len(files) > 1

    res = ""
    for file_name, line_number, line in matches:
        if append_file_name:
            res += f"{file_name}:"

        if append_line_number:
            res += f"{line_number}:"
        res += line

    return res


def render_file_names(matches, files):
    file_names = set()
    for file_name, *_rest in matches:
        file_names.add(file_name)
    res = ""
    for file_name in files:
        if file_name in file_names:
            res += file_name + "\n"
    return res


def match(line, pattern, flags):
    reflags = 0
    if flags.find("-i") != -1:
        reflags = re.I

    search_pattern = ".*" + pattern + ".*"
    if flags.find("-x") != -1:
        search_pattern = pattern

    found = re.match(search_pattern, line, reflags) is not None

    if flags.find("-v") != -1:
        found = not found

    return found


def render_line(line, line_number, flags):
    append_line_number = False
    if flags.find("-n") != -1:
        append_line_number = True

    res = ""
    if append_line_number:
        res += f"{line_number+1}:"

    res += line
    return res
