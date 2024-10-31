def calc_matrix(nelem, elem):
    # 係数マトリクスの計算
    for i in range(nelem):
        for j in range(3):
            coef = 0.25 / elem[i].det
            for k in range(3):
                term1 = elem[i].ex * elem[i].ce[j] * elem[i].ce[k]
                term2 = elem[i].ey * elem[i].de[j] * elem[i].de[k]
                elem[i].Se[j][k] = (term1 + term2) * coef
