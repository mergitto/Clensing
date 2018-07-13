########################################################
# 同じ文章をテキストコーパスから削除するためのスクリプト
########################################################

import calc
import pandas as pd
import sys

def create_text_list(filename):
    df = pd.read_csv(filename, header=None)
    df = df[0]
    df = df.str.split("\x20")
    text_list = list(df)
    return text_list

def save_text(text_list):
    f = open(sys.argv[2], 'w')
    for text in text_list:
        sentence = ""
        for word in text:
            sentence += word + " "
        sentence = sentence.rstrip()
        f.write(str(sentence) + "\n")
    f.close()

def delete_if_same(text_list):
    from tqdm import tqdm
    match_list = []
    origin_text_all_list = text_list[:]
    pop_count = 0
    print('[check same text]')
    for index, text in enumerate(tqdm(origin_text_all_list)):
        dummy_text_all_list = origin_text_all_list[:]
        dummy_text_all_list.pop(index)
        if text in dummy_text_all_list:
            # 現在のテキストのindexと、現在のテキストを抜かしたテキストのindexを追加する
            # これは、同じ文章が出てきたときには全ての中のテキストの中から、最初に出てくる同じテキストのindexを追加しておくことで
            # 処理後にカウントが2以上になる添字のものだけ、テキストの配列に追加することで、重複した文章を1つにするためである
            match_list.append(index)
            match_list.append(dummy_text_all_list.index(text))
            try:
                pop_index = index - pop_count
                text_list.pop(pop_index)
                pop_count += 1
            except:
                pass
    return match_list, text_list

def recovery_list(match_list, cleansing_text_list, origin_text_all_list):
    from collections import Counter
    counter = Counter(match_list)
    recovery_list = [i[0] for i in counter.items() if i[1] >= 2]
    for recovery_number in recovery_list:
        cleansing_text_list.append(origin_text_all_list[recovery_number])
    return cleansing_text_list


if __name__ == '__main__':
    calculation = calc.Calc()
    text_all_list = create_text_list(sys.argv[1])
    origin_text_all_list = text_all_list[:]

    match_list, cleansing_text_list = delete_if_same(text_all_list)
    recovery_text_list = recovery_list(match_list, cleansing_text_list, origin_text_all_list)

    save_text(recovery_text_list)

