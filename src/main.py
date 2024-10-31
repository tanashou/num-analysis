from read_mesh import read_mesh
from read_diri import read_diri
from calc_elem import calc_elem
from calc_matrix import calc_matrix
from calc_band import calc_band
from set_bound import set_bound
from set_coef import set_coef
from gauss import gauss
from draw import draw

# メッシュ読み込み
nelem, elem, nnode, node = read_mesh("mesh.dat")

# 固定境界読み込み
ndiri, diri, nbound = read_diri("diri.dat")

# 要素係数/面積の計算
calc_elem(nelem, elem, nnode, node)

# 全体要素係数の計算
calc_matrix(nelem, elem)

# 未知数の個数
np = nnode - nbound

# バンド幅、係数行列の計算
nband, matrix = calc_band(nelem, elem, np)

# 固定境界の設定
set_bound(nnode, node, ndiri, diri)

# 連立方程式の生成
set_coef(np, nband, matrix, nelem, elem, nnode, node)

# ガウスの消去法による連立1次方程式の解法
gauss(np, nband, matrix, node)

# ポテンシャルの出力
for i in range(nnode):
    print(i, ":", node[i].A)

# グラフの描画
draw(nelem, elem, nnode, node)
