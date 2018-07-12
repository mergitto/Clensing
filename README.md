# 日本語コーパス作成のための前処理機能の実装
日本語のコーパスを作成するためには、最初から単語の間にスペース区切りによって分かち書きされている英語よりも複雑な処理が必要となる

とりあえず日本語の文章をまとめたテキストあるから簡単に前処理して分かち書きした状態で出力する処理があれば便利なのにという思いからこの機能を作成した

実際には、プロジェクトや自然言語の形に合わせて前処理はやって行く必要があるが、自然言語の前処理の取っ掛かりとして参考になれば幸いです

### 環境
Python3以上


### 環境構築
[MeCabのインストール](https://www.saintsouth.net/blog/morphological-analysis-by-mecab-and-mecab-ipadic-neologd-and-python3/)
※ Macのかたはbrewとかでいけると思うので違う記事を参考にしてください
MeCab辞書であるipadic-neologdを入れるときにはpatchがないと怒られるので以下のコマンドを実行後、ipadic-neologdを入れる  
ipadic-neologdは結構容量を食うので余裕を持って入れるようにしてください
```
sudo yum install gcc-c++ libiconv patch
```
以下のコマンドが使えるようになれば大丈夫です
```
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
```

### 概要
1行ごとに日本語の文章が格納されたファイルを対象として簡単なクレンジング作業と分かち書きを行えるようにしています

[実行手順]
1. 分かち書きする
```
python wakati.py filename.csv newfilename.csv
```
1. ストップワードの除去をする
```
python stopword.py newfilename.csv updatefilename.csv
```
1. 類似文章を削除する
```
python carving.py updatefilename.csv cutfilename.csv
```
