from itertools import permutations


def can_chain(dominoes: list[tuple[int]]):
    if len(dominoes) == 0:
        return []

    for perm in permutations(dominoes, len(dominoes)):
        candidate_chain = list(perm)
        if len(candidate_chain) == 1:
            if candidate_chain[0][0] == candidate_chain[0][1]:
                return candidate_chain
            else:
                continue

        head = candidate_chain[0]
        tail = candidate_chain[-1]
        targets = set(head).intersection(set(tail))
        if len(targets) == 0:
            continue

        for target in targets:
            chain = chain_match_target(target, candidate_chain)
            if chain is not None:
                return chain

    return None


def chain_match_target(target: int, candidate: list[tuple[int]]) -> list[tuple[int]]:
    chain = []
    for d in candidate:
        if d[0] == target:
            chain.append(d)
            target = d[1]
        elif d[1] == target:
            chain.append((d[1], d[0]))
            target = d[0]
        else:
            return None

    head = chain[0]
    tail = chain[-1]
    if head[0] == tail[1]:
        return chain

    return None
