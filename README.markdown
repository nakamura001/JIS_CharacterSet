##JIS_X_0201.py
 JIS X 0201 の文字を Unicode に変換するテーブルファイルの情報を元に JIS X 0201 の文字一覧を取得。

##JIS_X_0208.py
 JIS X 0208 の文字を Unicode に変換するテーブルファイルの情報を元に JIS X 0208 の文字一覧を取得。

##JIS_X_0212.py
 JIS X 0212 の文字を Unicode に変換するテーブルファイルの情報を元に JIS X 0212 の文字一覧を取得。

##SHIFTJIS.py
 Shift-JIS の文字を Unicode に変換するテーブルファイルの情報を元に Shift-JIS の文字一覧を取得。

##SHIFTJIS_custom/SHIFTJIS_custom_bom_utf8.txt
*BOM有りUTF-8
* ~ (チルダ)に対応するUnicodeが ?(OVERLINE) となっている為、 TILDE(U+007E) に置き換え。

##SHIFTJIS_custom/SHIFTJIS_custom_utf8.txt
*BOM無しUTF-8
* ~ (チルダ)に対応するUnicodeが ?(OVERLINE) となっている為、 TILDE(U+007E) に置き換え。

##SHIFTJIS_custom/SHIFTJIS_custom_win_bom_utf8.txt
*BOM有りUTF-8
* ~ (チルダ)に対応するUnicodeが ?(OVERLINE) となっている為、 TILDE(U+007E) に置き換え。
* ['DOUBLE VERTICAL LINE' (U+2016) ](http://www.fileformat.info/info/unicode/char/2016/index.htm)を ['PARALLEL TO' (U+2225) ](http://www.fileformat.info/info/unicode/char/2225/index.htm)に置き換え。


##参考
JIS0201.TXTの配布場所。
<http://unicode.org/Public/MAPPINGS/OBSOLETE/EASTASIA/JIS/JIS0201.TXT>

JIS0208.TXTの配布場所。
<http://unicode.org/Public/MAPPINGS/OBSOLETE/EASTASIA/JIS/JIS0208.TXT>

JIS0212.TXTの配布場所。
<http://unicode.org/Public/MAPPINGS/OBSOLETE/EASTASIA/JIS/JIS0212.TXT>

SHIFTJIS.TXTの配布場所。
<http://unicode.org/Public/MAPPINGS/OBSOLETE/EASTASIA/JIS/SHIFTJIS.TXT>