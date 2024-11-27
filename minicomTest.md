```bash
sudo apt-get install minicom
sudo minicom -s
```
「Serial port setup」 を選択
「A - Serial Device」 を /dev/ttyS0 に設定
「E - Bps/Par/Bits」 を 9600 8N1 に設定（必要に応じてボーレートを変更）
「F - Hardware Flow Control」 を 「No」 に設定
「G - Software Flow Control」 を 「No」 に設定

minicom の起動

sudo minicom
AT コマンドの送信

SIM7080G に対して AT コマンドを送信し、応答を確認します。

AT
期待される応答：

OK
注意: 応答がない場合、配線や設定を再確認してください。

minicom の終了

Ctrl + A を押してから X を押し、minicom を終了します。