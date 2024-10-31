def set_coef(np, nband, matrix, nelem, elem, nnode, node):  # 各行列要素を初期化
    # 各行列要素を初期化
    for i in range(np):
        for j in range(matrix[i].nk):
            matrix[i].h.append(0.0)

    for i in range(nelem):
        for j in range(3):
            l = elem[i].node[j]
            if l > np:
                continue

            for k in range(3):
                m = elem[i].node[k]
                if m > np:
                    continue
                elif m < 1:
                    continue

                node[l - 1].A -= elem[i].Se[j][k] * node[m - 1].A
                matrix[l - 1].h[m - 1] += elem[i].Se[j][k]
