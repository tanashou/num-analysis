from Fem2D import Elem, Node


def ReadMesh(filename):  # メッシュの読み込み
    nelem = 0  # 要素数
    elem = []  # 要素配列
    nnode = 0  # 節点数
    node = []  # 節点配列

    with open(filename, "r") as file:
        item = file.readline().strip().split()  # 空白で区切る
        nelem = int(item[0])
        nnode = int(item[1])

        for i in range(nelem):
            item = file.readline().strip().split()  # 要素データ
            e = Elem()
            e.node[0] = int(item[0])
            e.node[1] = int(item[1])
            e.node[2] = int(item[2])
            elem.append(e)

        for i in range(nnode):
            item = file.readline().strip().split()  # 節点座標
            n = Node()
            n.x = float(item[0])
            n.y = float(item[1])
            node.append(n)

    print(f"nelem = {nelem}, nnode = {nnode}")
    return nelem, elem, nnode, node
