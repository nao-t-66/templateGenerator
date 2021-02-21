# templateGenerator
html generator from template and csv  

### usage  
```
python3 generate.py
```
  
- template.htmlに記載したHTML中の`{%`と`%}`で囲まれた中の文字列の箇所を、CSVの1行目の文字列と一致した列の文字で置き換えます。  
CSVの1行目がキーワード行、2行目以降がコンテンツ行です。  
- 2行目以降は1行ごとに1HTMLファイル生成されます。  
- キーワード行の一番左の文字列を「filename」にすると、各行のHTMLファイルのファイル名が「コンテンツ行に入力した名前.html」になります。
  
### options  
- template html file path  
```
python3 generate.py --template [html path]
```  
  
- source csv file path  
```
python3 generate.py --source [csv path]  
```
  
- output directory path  
```
python3 generate.py --output [directory path]  
```
