import serial
import time

# シリアルポートの設定
ser = serial.Serial('/dev/ttyAMA0', 9600)

# 初期化処理
def send_at_command(command, wait_for_response=True):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode()
    if not bool(response):
        return send_at_command(command, wait_for_response)
    print(f"Response: {response}")
    return response

# ATコマンドでモジュールが応答するか確認
send_at_command('AT')

# SIMカードの状態を確認
send_at_command('AT+CPIN?')

# ネットワーク登録状態の確認
send_at_command('AT+CGATT?')

# 終了処理
ser.close()
