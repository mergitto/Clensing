##################################
# テキストファイルを分かち書きする
##################################
## python wakati.py 読み込むテキスト.txt 書き込むテキスト.txt

import MeCab
import sys

tagger = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati')


fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
    result = tagger.parse(line)
    fo.write(result[0:])
    line = fi.readline()

fi.close()
fo.close()

