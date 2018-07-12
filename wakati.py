##################################
# テキストファイルを分かち書きする
##################################
## python wakati.py 読み込むテキスト.txt 書き込むテキスト.txt

import sys
from parse import parser_space

fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
    result = parser_space(line)
    fo.write(result[0:])
    line = fi.readline()

fi.close()
fo.close()

