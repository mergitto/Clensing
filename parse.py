# -*- coding: utf-8 -*-

from natto import MeCab
mc = MeCab('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

def parser_mecab(text):
    words = []
    for n in mc.parse(text, as_nodes=True):
        node = n.feature.split(',');
        if node[0] != '助詞' and node[0] != '助動詞' and node[0] != '記号' and node[1] != '数':
        #if node[0] != '助詞' and node[0] != '助動詞' and node[0] != '記号' and node[1] != '数' and node[0] != '動詞' and node[0] != '副詞':
            if node[0] == '動詞':
                words.append(node[6])
            elif node[0] == 'BOS/EOS':
                continue
            else:
                words.append(n.surface)
    return words

def is_noun(word):
    for n in mc.parse(word, as_nodes=True):
        node = n.feature.split(',');
        if node[0] == '名詞':
            return True
        else:
            return False

def parser_space(text):
    words = ""
    for n in mc.parse(text, as_nodes=True):
        node = n.feature.split(',');
        if node[0] != '助詞' and node[0] != '助動詞' and node[0] != '記号' and node[1] != '数':
            if node[0] == '動詞':
                words += node[6]
            elif node[0] == 'BOS/EOS':
                continue
            else:
                words += n.surface
        words += " "
    return words


