##################################
# テキストファイルを分かち書きする
#
# もし分かち書きをカンマにしたいときは
# parser_mecabをimportするようにする
##################################
## python wakati.py 読み込むテキスト.csv 書き込むテキスト.csv

import sys
from parse import parser_space

def wakati():
    fi = open(sys.argv[1], 'r')
    fo = open(sys.argv[2], 'w')

    line = fi.readline()
    while line:
        result = parser_space(line)
        fo.write(result[0:])
        line = fi.readline()

    fi.close()
    fo.close()

if __name__ == '__main__':
    wakati()

