from Fem2D import Matrix


def CalcBand(nelem, elem, np):  # バンド幅，係数行列の計算
    nband = 0  # バンド幅
    matrix = [Matrix() for _ in range(np)]  # 係数行列
    for i in range(nelem):
        for j in range(3):
            l = elem[i].node[j]
            if l > np:
                continue
            if l < 1:
                continue
            for k in range(3):
                m = elem[i].node[k]
                if m > np or m < 1:
                    continue
                nd = m - l + 1
                if nd > matrix[l - 1].nk:
                    matrix[l - 1].nk = nd

    # 最大バンド幅の計算
    nband = matrix[0].nk
    for i in range(1, np):
        j = i
        nd = matrix[j - 1].nk - 1  # インデックスの調整
        if matrix[i].nk < nd:
            matrix[i].nk = nd
        if nband < matrix[i].nk:
            nband = matrix[i].nk

    print(f"np = {np}, nband = {nband}")
    return nband, matrix
