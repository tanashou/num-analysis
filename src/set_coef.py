def set_coef(np, nband, matrix, nelem, elem, nnode, node):
    # Initialize matrix elements
    for i in range(np):
        matrix[i].h = [0.0] * matrix[i].nk

    for i in range(nelem):
        for j in range(3):
            l = elem[i].node[j]
            if l > np or l < 1:
                continue

            for k in range(3):
                m = elem[i].node[k]
                if m > np:
                    node[l - 1].A -= elem[i].Se[j][k] * node[m - 1].A
                elif m < 1:
                    continue
                else:
                    # Calculate the position in the band matrix
                    pos = m - l
                    if 0 <= pos < matrix[l - 1].nk:
                        matrix[l - 1].h[pos] += elem[i].Se[j][k]
