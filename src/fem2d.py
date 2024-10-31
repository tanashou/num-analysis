eair = 1.0  # 磁界解析では真空の透磁率を与える


class Elem:  # 要素クラス
    def __init__(self):
        self.node = [0, 0, 0]  # 節点番号
        self.cje = [0, 0, 0]  # 要素係数 cje
        self.dje = [0, 0, 0]  # 要素係数 dje
        self.Se = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 要素係数マトリクス
        self.delt = 0.0  # 面積
        self.ex = eair  # 材料定数
        self.ey = eair  # 材料定数


class Node:  # 節点クラス
    def __init__(self):
        self.x = 0.0  # x座標
        self.y = 0.0  # y座標
        self.A = 0.0  # ポテンシャル


class Diri:  # 固定境界クラス
    def __init__(self):
        self.ns = 0  # 開始節点
        self.ne = 0  # 終了節点
        self.A = 0.0  # 固定ポテンシャル


class Matrix:  # マトリクスクラス
    def __init__(self):
        self.h = []  # 係数マトリクスの要素
        self.nk = 0  # 半バンド幅
