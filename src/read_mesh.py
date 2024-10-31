from fem2d import Elem, Node


def read_mesh(filename):  # メッシュの読み込み
    elem = []  # 要素配列
    nnode = 0  # 節点数
    node = []  # 節点配列

    with open(filename, "r") as file:
        item = file.readline().strip().split()  # 要素数と節点数を読み込み
        nelem = int(item[0])
        nnode = int(item[1])

        for i in range(nelem):
            item = file.readline().strip().split()  # 要素のノードを読み込み
            e = Elem()
            e.node[0] = int(item[0])
            e.node[1] = int(item[1])
            e.node[2] = int(item[2])
            elem.append(e)

        for i in range(nnode):
            item = file.readline().strip().split()  # 節点座標を読み込み
            n = Node()
            n.x = float(item[0])
            n.y = float(item[1])
            node.append(n)

    print(f"nelem = {nelem}, nnode = {nnode}")
    return nelem, elem, nnode, node
