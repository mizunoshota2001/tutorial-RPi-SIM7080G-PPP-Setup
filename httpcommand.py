import serial
import time

# シリアルポートの設定
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

# インターネット接続とHTTPリクエスト送信
def send_at_command(command, wait_for_response=True):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode()
    if not bool(response):
        return send_at_command(command, wait_for_response)
    print(f"Response: {response}")
    return response

def send_http_request():
    # PINコードの入力
    send_at_command('AT+CPIN="0000"')

    # 機能設定
    send_at_command('AT+CFUN=1')

    # APN設定
    send_at_command('AT+CGDCONT=1,"IP","ppsim.jp","0.0.0.0",0,0,0,440,03')

    # GPRS接続を開始
    send_at_command('AT+CGACT=1,1')

    # ダイヤルアップ接続
    send_at_command('ATD*99#')

    # HTTP接続開始
    send_at_command('AT+HTTPINIT')

    # HTTPサーバーの設定
    send_at_command('AT+HTTPPARA="URL","http://example.com"')

    # HTTPリクエスト送信
    send_at_command('AT+HTTPACTION=0')  # GETリクエスト
    time.sleep(3)

    # レスポンスを取得
    send_at_command('AT+HTTPREAD')

    # HTTPセッション終了
    send_at_command('AT+HTTPTERM')

# HTTPリクエスト送信
send_http_request()

# 終了処理
ser.close()
