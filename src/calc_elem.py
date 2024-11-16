def CalcElem(nelem, elem, nnode, node):  # 係数/面積の計算
    for i in range(nelem):
        j1 = elem[i].node[0] - 1
        j2 = elem[i].node[1] - 1
        j3 = elem[i].node[2] - 1

        elem[i].cje[0] = node[j2].y - node[j3].y
        elem[i].cje[1] = node[j3].y - node[j1].y
        elem[i].cje[2] = node[j1].y - node[j2].y

        elem[i].dje[0] = node[j3].x - node[j2].x
        elem[i].dje[1] = node[j1].x - node[j3].x
        elem[i].dje[2] = node[j2].x - node[j1].x

        elem[i].delt = 0.5 * (
            elem[i].cje[1] * elem[i].dje[2] - elem[i].cje[2] * elem[i].dje[1]
        )
