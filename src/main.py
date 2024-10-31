from ReadMesh import ReadMesh
from ReadDiri import ReadDiri
from CalcElem import CalcElem
from CalcMatrix import CalcMatrix
from CalcBand import CalcBand
from SetBound import SetBound
from SetCoef import SetCoef
from Gauss import Gauss
from Draw import Draw

nelem, elem, nnode, node = ReadMesh("mesh.dat")  # メッシュ読み込み
ndiri, diri, nbound = ReadDiri("diri.dat")  # 境界条件読み込み
CalcElem(nelem, elem, nnode, node)  # 要素係数/面積の計算
CalcMatrix(nelem, elem)  # 全体要素係数の計算
np = nnode - nbound  # 未知数の個数
nband, matrix = CalcBand(nelem, elem, np)  # バンド幅，係数行列の計算
SetBound(nnode, node, ndiri, diri)  # 固定境界の設定
SetCoef(np, nband, matrix, nelem, elem, nnode, node)  # 連立方程式の生成
Gauss(np, nband, matrix, node)  # ガウスの消去法による連立1次方程式の解法

### ポテンシャルの出力
for i in range(nnode):
    print(i, ":", node[i].A)

Draw(nelem, elem, nnode, node)  # メッシュ描画
