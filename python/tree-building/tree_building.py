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
    if not all(r.parent_id < r.record_id or r.parent_id == 0 for r in records):
        raise ValueError('parent id should be lower than'
                         'record id except for root')

    tree = [Node(record.record_id) for record in records]

    for record in records[1:]:
        tree[record.parent_id].children.append(tree[record.record_id])

    if len(tree) > 0:
        root = tree[0]
    else:
        root = None

    return root
