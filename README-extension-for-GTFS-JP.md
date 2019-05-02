# extensions/GTFS-JP

## これは何？

Googleの[FeedValidator](https://github.com/google/transitfeed/wiki/FeedValidator)で，標準的なバス情報フォーマット(GTFS-JP)も検証できるようにするための拡張です。

## 作った背景

素のFeedValidatorを用いて標準的なバス情報フォーマット(GTFS-JP)ファイルの検証を行った場合には，以下のような課題が生じます。

- 標準のGTFSには含まれないファイル(agency-jp.txt等)がUnknown Fileと言われる。
- 標準のGTFSには含まれない項目(jp_parent_route_id等)がUnrecognized Columnと言われる。
- 標準のGTFSには含まれないファイルや項目については各種チェックがなされない。

これらの課題を解決するためにこの拡張を作成しました。

## 使い方

### 初回のみの準備

#### gitを使う場合

````sh
git clone https://github.com/google/transitfeed.git
cd transitfeed/extensions
git clone https://github.com/kuwayamamasayuki/GTFS-JP.git
cd ..
````

#### gitなど使いたくない or 使えないという場合

1. python（２系）がインストールされていない場合にはpythonをインストールする。
1. 次のリンクからtransitfeedダウンロードする。[https://github.com/google/transitfeed/archive/1.2.16.zip](https://github.com/google/transitfeed/archive/1.2.16.zip)
1. ダウンロードしたファイルを展開する。
1. `cd transitfeed-1.2.16/extensions/`
1. 次のリンクからGTFS-JP拡張をダウンロードする。[https://github.com/kuwayamamasayuki/GTFS-JP/archive/master.zip](https://github.com/kuwayamamasayuki/GTFS-JP/archive/master.zip)
1. ダウンロードしたGTFS-JP拡張を展開する。
1. 展開してできたフォルダ「GTFS-JP-master」の名前を「GTFS-JP」に変更する。
1. `cd ..` して，feedvalidator.pyのあるフォルダに移動する。

### 実際の使用

````sh
python feedvalidator.py --extension=extensions.GTFS-JP (対象のGTFSファイルやフォルダ)
````

## 出力結果例

次の図は，福岡県古賀市のコガバス（古賀市公共施設等連絡バス）のデータを，テスト用にわざと誤りが含まれるように修正したものを検証した結果の一部です。
![出力例](キャプチャ.png)

## 既知のバグ

いくつかの警告については，HTMLファイルに出力されず，標準出力に出力されてしまいます。

このため，「feed validated successfully」と表示されたからといって安心しきってはいけません。
feedvalidator.pyを起動した画面も確認してください。

標準出力に出力されてしまう警告の例としては，以下のようなものがあります。

- 田沼下町 (ID 24_1) is too far from its parent station 田沼下町 (ID 24) : 107.26 meters.
- The stops "高崎バスセンター" (ID 236_02) and "高崎バスセンター" (ID H0006_01) are 0.00m apart and probably represent the same location.