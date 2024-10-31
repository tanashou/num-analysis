import matplotlib.pyplot as plt


def draw(nelem, elem, nnode, node):
    # グラフのセットアップ
    fig = plt.figure()
    graph = fig.add_subplot(111)
    graph.set_xlim([-2, 8])
    graph.set_ylim([-2, 8])

    # カラーマップ
    color = [
        "#8a008a",
        "#3200ff",
        "#008aff",
        "#00ffaf",
        "#00ff00",
        "#80ff55",
        "#ffff00",
        "#ffd500",
        "#ffa000",
        "#ff8a00",
        "#ff0000",
    ]

    # 三角要素の描画
    for i in range(nelem):
        n1, n2, n3 = elem[i].node[0], elem[i].node[1], elem[i].node[2]
        x1, y1 = node[n1 - 1].x, node[n1 - 1].y
        x2, y2 = node[n2 - 1].x, node[n2 - 1].y
        x3, y3 = node[n3 - 1].x, node[n3 - 1].y

        tri = plt.Polygon(((x1, y1), (x2, y2), (x3, y3)), fc="#ffffaa", ec="#000000")
        graph.add_patch(tri)

    # 各節点の描画
    for i in range(nnode):
        x, y = node[i].x, node[i].y
        col = color[int(node[i].A) % len(color)]
        circle = plt.Circle((x, y), 0.15, fc=col)
        graph.add_patch(circle)

    plt.show()
