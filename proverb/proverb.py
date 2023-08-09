def proverb(*data, qualifier):
    sentences = list()
    l = len(data)
    if l == 0:
        return sentences

    i = 0
    while i < l-1:
        sentences.append(f"For want of a {data[i]} the {data[i+1]} was lost.")
        i += 1

    prefix = ""
    if qualifier != None:
        prefix = qualifier + " "

    sentences.append(f"And all for the want of a {prefix}{data[0]}.")

    return sentences
