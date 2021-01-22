class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)

    if not all(r.record_id == i for i, r in enumerate(records)):
        raise ValueError('Records should be continueous starting from 0')
    if not all(r.parent_id == 0 or r.parent_id < r.record_id for r in records):
        raise ValueError('parent id should be lower than'
                         'record id except for root')

    trees = [Node(record.record_id) for record in records]

    parent = {}
    ordered_id = [i.record_id for i in records]
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    root = None
    if len(trees) > 0:
        root = trees[0]
    return root
