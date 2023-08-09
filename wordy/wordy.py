import re

matcher = re.compile(r'^What is (-?\d+).*\?$')

def operation(name, a, b):
    if name == "plus":
        return a + b
    elif name == "minus":
        return a - b
    elif name == "multiplied":
        return a * b
    elif name == "divided":
        return a / b
    else:
        raise ValueError("unknown operation")

# def answer(question):
#     initial_match = re.match(r'What is (-?\d+)', question)
#     if initial_match == None:
#         raise ValueError("syntax error")

#     res = int(initial_match.group(1))

#     for m in re.finditer(r'\s(\D+)\s(-?\d+)', question[initial_match.end():]):
#         res = operation(m.group(1), res, int(m.group(2)))
            
#     return res

def is_operator(t):
    return re.match(r'[a-z]+', t) != None

def is_operand(t):
    return re.match(r'-?\d+', t) != None

def answer(question):
    if question == "What is?":
        raise ValueError("syntax error")
    
    initial_match = re.match(r'^What is (.*)\?$', question)
    if initial_match == None:
        raise ValueError("unknown operation")

    tokens = list(initial_match.group(1).split(" "))
    if not is_operand(tokens[0]):
        raise ValueError("syntax error")
    
    res = int(tokens[0])

    expect_operator = True
    operator = ""
    expect_operand = False
    operand = ""
    expect_by = False
    for t in tokens[1:]:
        if expect_operator:
            if not is_operator(t):
                raise ValueError("syntax error")
            
            if not t in ["plus", "minus", "multiplied", "divided"]:
                raise ValueError("unknown operation")

            operator = t
            expect_operator = False
            if t == "multiplied" or t == "divided":
                expect_by = True
            else:
                expect_operand = True
            continue
        
        if expect_by:
            if t != "by":
                raise ValueError("syntax error")
            
            expect_by = False
            expect_operand = True
            continue

        if expect_operand:
            if not is_operand(t):
                raise ValueError("syntax error")
            
            operand = int(t)
            res = operation(operator, res, operand)
            expect_operand = False
            expect_operator = True
            continue
    
    if expect_operand:
        raise ValueError("syntax error")

    return res