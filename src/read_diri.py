from fem2d import Diri


def ReadDiri(filename):
    ndiri = 0  # 固定領域数
    diri = []  # 固定境界配列
    nbound = 0  # 固定境界節点数

    with open(filename, "r") as file:
        ndiri = int(file.readline().strip())  # 固定境界数
        for i in range(ndiri):
            item = file.readline().strip().split()  # 空白で区切り、不要な空白も除去
            diri.append(Diri())
            diri[i].ns = int(item[0])
            diri[i].ne = int(item[1])
            diri[i].A = float(item[2])
            nbound += diri[i].ne - diri[i].ns + 1

    print(f"ndiri = {ndiri}, nbound = {nbound}")
    return ndiri, diri, nbound
