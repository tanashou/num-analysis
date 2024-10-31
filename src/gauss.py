def Gauss(np, nband, matrix, node):  # ガウスの消去法による連立1次方程式の解法
    # 前進消去
    mnp = np - 1
    for i in range(mnp):
        if matrix[i].h[0] == 0:
            raise ZeroDivisionError(f"Zero pivot encountered at row {i}.")
        r = 1.0 / matrix[i].h[0]
        nb = min(matrix[i].nk, nband)  # 帯域制限
        for j in range(1, nb):
            q = r * matrix[i].h[j]
            ij = i + j
            if ij >= np:
                break  # 範囲外アクセス
            for k in range(j, nb):
                kj = k - j
                matrix[ij].h[kj] -= q * matrix[i].h[k]
            node[ij].A -= q * node[i].A
        matrix[i].h[j] = q  # 更新して次の反復で使用
        node[i].A *= r

    # 後退代入
    if matrix[np - 1].h[0] == 0:
        raise ZeroDivisionError("Zero pivot encountered at the last row.")
    node[np - 1].A /= matrix[np - 1].h[0]
    for i in range(np - 2, -1, -1):
        nb = min(matrix[i].nk, nband)  # 帯域制限
        for j in range(1, nb):
            if i + j >= np:
                break  # 範囲外アクセス
            node[i].A -= matrix[i].h[j] * node[i + j].A
