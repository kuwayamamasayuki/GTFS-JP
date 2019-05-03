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

1. `git clone https://github.com/google/transitfeed.git`
1. `cd transitfeed/extensions`
1. `git clone https://github.com/kuwayamamasayuki/GTFS-JP.git`
1. `cd ..`
1. feedvalidator.pyの593行目，RunValidation()の中でschedule.Validate()を呼び出しているところの引数として，「problems=problems」を追加。
もう少し具体的に言うと，
````
  schedule.Validate(service_gap_interval=options.service_gap_interval,
                    validate_children=False)
````
の部分を，
````
  schedule.Validate(service_gap_interval=options.service_gap_interval,
                    validate_children=False, problems=problems)
````
に変更する必要があります。


#### gitなど使いたくない or 使えないという場合

1. python（２系）がインストールされていない場合にはpythonをインストールする。
1. 次のリンクからtransitfeedダウンロードする。[https://github.com/google/transitfeed/archive/1.2.16.zip](https://github.com/google/transitfeed/archive/1.2.16.zip)
1. ダウンロードしたファイルを展開する。
1. `cd transitfeed-1.2.16/extensions/`
1. 次のリンクからGTFS-JP拡張をダウンロードする。[https://github.com/kuwayamamasayuki/GTFS-JP/archive/master.zip](https://github.com/kuwayamamasayuki/GTFS-JP/archive/master.zip)
1. ダウンロードしたGTFS-JP拡張を展開する。
1. 展開してできたフォルダ「GTFS-JP-master」の名前を「GTFS-JP」に変更する。
1. `cd ..` して，feedvalidator.pyのあるフォルダに移動する。
1. feedvalidato.pyを修正（上の「gitを使う場合」の5.と同じ。）

### 実際の使用

````sh
python feedvalidator.py --extension=extensions.GTFS-JP (対象のGTFSファイルやフォルダ)
````

## 出力結果例

次の図は，福岡県古賀市のコガバス（古賀市公共施設等連絡バス）様のデータを，テスト用にわざと誤りが含まれるように修正したものを検証した結果の一部です。
![出力例](キャプチャ.PNG)

これ以外の各交通事業者のGTFSファイルを検証した結果は，[http://35.192.87.3/FeedValidator-extension-for-GTFS-JP/output.html](http://35.192.87.3/FeedValidator-extension-for-GTFS-JP/output.html)にあります。
後述のバグのせいで，各交通事業者につき，HTMLファイルとTXTファイルの二つをご確認いただく必要があります。
また，2019/4/30～5/1にかけてダウンロードしたデータを用いて検証したものですので，最新の情報ではないかもしれません。

## 主な拡張内容

- extensions.GTFS-JP.GtfsFactory:
  - 'agency_jp.txt', 'route_jp.txt', 'office_jp.txt', 'translations.txt' を追加
  - 'fare_attributes.txt' 及び 'feed_info.txt' が必須であることを追加

- extensions.GTFS-JP.Agency:
  - 'agency_id'が必須項目であることの確認の追加
  - 'agency_timezone'が'Asia/Tokyo'（固定文字列）であることの確認を追加
  - 'agency_lang'が'ja'（固定文字列）であることの確認を追加

- extensions.GTFS-JP.Agency_jp
  - 'agency_id'が必須項目であることの確認を追加
  - 'agency_zip_number'がハイフンなしの半角７桁であることの確認を追加
  - 'agency_president_name'で，姓と名の間に全角スペース１文字があることの確認を追加

- extensions.GTFS-JP.Stop
  - 'platform_code'を追加
  - 'stop_timezone'が設定されていた場合，不要である旨警告を出すようにした
  - 'wheelchair_boarding'が設定されていた場合，不要である旨警告を出すようにした

- extensions.GTFS-JP.Route
  - 'agency_id'が必須項目であることの確認を追加
  - 'route_type'が'3'（固定値）であることの確認を追加
  - 'jp_parent_route_id'（任意項目）を追加

- extensions.GTFS-JP.Route_jp
  - 'route_id'が必須項目であることの確認を追加
  - 'route_update_dateが適切な書式の日付であるかどうかの確認を追加

- extensions.GTFS-JP.Trip
  - 'jp_trip_desc', 'jp_trip_desc_symbol', 'jp_office_id'（いずれも任意項目）を追加
  - 'jp_office_id'の値が，'office_jp.txt'内で定義されているかの確認を追加

- extensions.GTFS-JP.Office_jp
  - 'office_id'及び'office_name'が必須項目であることの確認を追加
  - 'office_url'が有効なURLであることの確認を追加

- extensions.GTFS-JP.FareAttribute
  - 'currency_type'の値が'JPY'（固定値）であることの確認を追加

- extensions.GTFS-JP.FareRules
  - 'contains_id'が設定されていた場合，不要である旨警告を出すようにした

- extensions.GTFS-JP.Shape
  - 'shape_dist_traveled'が設定されていた場合，不要である旨警告を出すようにした

- extensions.GTFS-JP.feed_info
  - 'feed_lang'の値が'ja'（固定値）であることの確認を追加

- extensions.GTFS-JP.Translations
  - 'trans_id', 'lang', 'translation'が必須項目であることの確認を追加
  
- extensions.GTFS-JP.Schedule
  - GTFSとGTFS-JPとのrouteの使い方の違い（※）により，
  「Invalid value ○○ in field route_long_name
   The same combination of route_short_name and route_long_name shouldn't be used for more than one route, as it is for the for the two routes with IDs "△△" and "□□".」という警告メッセージが出ていたが，これを出ないようにした。
   ※ GTFSでは，往路・復路，経由違いや途中止まりを同一経路とするが，GTFS-JPでは，原則，経路を通過停留所別・方向別に分けるという点。 

## 既知のバグ

（2019/5/3時点ではありません。）


