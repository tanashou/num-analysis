def CalcMatrix(nelem, elem):  # 係数マトリクスの計算
    for i in range(nelem):
        for j in range(3):
            coef = 0.25 / elem[i].delt
            for k in range(3):
                term1 = elem[i].ex * elem[i].cje[j] * elem[i].cje[k]
                term2 = elem[i].ey * elem[i].dje[j] * elem[i].dje[k]
                elem[i].Se[j][k] = (term1 + term2) * coef
