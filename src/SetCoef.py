def SetCoef(np, nband, matrix, nelem, elem, nnode, node):  # 連立方程式の係数設定
    # 各行列要素を初期化
    for i in range(np):
        for j in range(matrix[i].nk):
            matrix[i].h += [0.0]

    for i in range(nelem):
        for j in range(3):
            l = elem[i].node[j]
            if l > np:
                continue
            for k in range(3):
                m = elem[i].node[k]
                if m > np:
                    node[l - 1].A -= elem[i].Se[j][k] * node[m - 1].A
                elif m < l:
                    continue
                else:
                    matrix[l - 1].h[m - l] += elem[i].Se[j][k]
