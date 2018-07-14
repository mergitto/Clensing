##################################
# テキストファイルを分かち書きする
#
# もし分かち書きをカンマにしたいときは
# parser_mecabをimportするようにする
##################################
## python wakati.py 読み込むテキスト.csv 書き込むテキスト.csv

import sys
from parse import parser_space
from tqdm import tqdm

def wakati():
    fi = open(sys.argv[1], 'r')
    fo = open(sys.argv[2], 'w')

    text_data = fi.read()
    fi.close()
    lines = text_data.split('\n')
    print('[wakati text & save text]')
    for line in tqdm(lines):
        result = parser_space(line)
        result += "\n"
        fo.write(result[0:])

    fo.close()

if __name__ == '__main__':
    wakati()

