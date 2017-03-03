class Node():
    def __init__(self, point, dimention):
        self.right = []
        self.left = []
        self.point = point
        self.dimention = dimention

def median(data):
    try:
        m = int(len(data) / 2)
        return data[m], m
    except Exception:
        pass

def build_tree(data, dimention, count, node_list):
    try:
        data = sorted(data, key = lambda x: x[dimention])
        data_median, index_medina = median(data)
        del data[index_medina]
        node_list.append(Node(data_median,dimention))
        node_list[count].left = data[:index_medina]
        node_list[count].right = data[index_medina:]
        dimention = not dimention
        count += 1
        if index_medina > 0 :build_tree(data[:index_medina],dimention, count, node_list)
        if len(data) > 1 :build_tree(data[index_medina:], dimention, count, node_list)
        return node_list
    except Exception:
        pass

def train(data):
    node_list = []
    dimention = False
    count = 0
    node_list = build_tree(data, dimention, count, node_list)

    for i in range(len(node_list)):
        print(node_list[i].point, node_list[i].dimention)

T = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]

train(T)
