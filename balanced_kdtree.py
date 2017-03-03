class Node:
    def __init__(self, point, dimension, depth, left=[], right=[]):
        self.left = left
        self.right = right
        self.point = point
        self.dimension = dimension
        self.depth = depth


def median(data):
    m = int(len(data) / 2)
    return data[m], m


def build_tree(data, dimension, node_list, k, depth=0):
    if depth < k:
        data = sorted(data, key=lambda x: x[dimension])
        data_median, index_medina = median(data)
        del data[index_medina]
        node_list.append(Node(data_median, dimension, depth, left=data[:index_medina],
                              right=data[index_medina:]))
        depth += 1
        if index_medina > 0: build_tree(data[:index_medina], not dimension, node_list, k, depth=depth)
        if len(data) > 1: build_tree(data[index_medina:], not dimension, node_list, k, depth=depth)
    return node_list


def train(data):
    node_list = []
    dimension = False
    node_list = build_tree(data, dimension, node_list, k=3)

    for i in range(len(node_list)):
        print("node:", i, "\tpoint:", node_list[i].point, "\tdepth:", node_list[i].depth,
              "\tdimension:", node_list[i].dimension, "\tleft:", node_list[i].left,
              "right:", node_list[i].right)


T = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
train(T)
