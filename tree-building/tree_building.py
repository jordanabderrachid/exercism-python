from typing import List


class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def BuildTree(records: List[Record]):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if records:
        if ordered_id[0] != 0:
            raise ValueError("Record id is invalid or out of order.")

        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError("Record id is invalid or out of order.")
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for record in records:
            if ordered_id[i] == record.record_id:
                if record.parent_id > record.record_id:
                    raise ValueError(
                        "Node parent_id should be smaller than it's record_id."
                    )

                if record.record_id == 0:
                    if record.parent_id != 0:
                        raise ValueError("error!")

                if record.record_id == record.parent_id:
                    if record.record_id != 0:
                        raise ValueError(
                            "Only root should have equal record and parent id."
                        )
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for tree in trees:
            if i == tree.node_id:
                parent = tree
        for record in records:
            if record.parent_id == i:
                for tree in trees:
                    if tree.node_id == 0:
                        continue
                    if record.record_id == tree.node_id:
                        child = tree
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
