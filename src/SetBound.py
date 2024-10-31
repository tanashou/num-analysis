def SetBound(nnode, node, ndiri, diri):  # 固定境界の設定
    for i in range(nnode):
        node[i].A = 0.0

    for i in range(ndiri):
        start = max(0, diri[i].ns - 1)
        end = min(nnode, diri[i].ne)
        for j in range(start, end):
            node[j].A = diri[i].A
