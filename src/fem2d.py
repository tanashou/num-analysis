eair = 1.0  # 磁界解析では真空の透磁率を与える


class Elem:  # 要素
    def __init__(self):
        self.node = [0, 0, 0]  # ノード
        self.ce = [0, 0, 0]  # 要素係数 ce
        self.de = [0, 0, 0]  # 要素係数 de
        self.Se = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 要素係数マトリクス
        self.delt = 0.0  # 面積
        self.ex = eair  # 材料定数
        self.ey = eair  # 材料定数


class Node:  # 節点
    def __init__(self):
        self.x = 0.0  # x座標
        self.y = 0.0  # y座標
        self.A = 0.0  # ポテンシャル


class Diri:  # ディリクレ境界条件
    def __init__(self):
        self.ns = 0  # 開始節点
        self.ne = 0  # 終了節点
        self.A = 0.0  # 固定ポテンシャル


class Matrix:  # マトリクス
    def __init__(self):
        self.h = []  # 係数マトリクスの要素
        self.nk = 0  # 半バンド幅
