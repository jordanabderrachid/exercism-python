open_bracket_set = set("([{")
close_bracket_set = set("}])")
matching_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
}

def is_paired(input_string):
    closing_bracket_expected_stack = list()
    for c in input_string:
        if c in open_bracket_set:
            closing_bracket_expected_stack.append(matching_pairs[c])
        elif c in close_bracket_set:
            if len(closing_bracket_expected_stack) == 0:
                return False # found closing bracket that does not match an opened one

            e = closing_bracket_expected_stack.pop()
            if e != c:
                return False # mismatched opening and closing brackets
    
    return len(closing_bracket_expected_stack) == 0
