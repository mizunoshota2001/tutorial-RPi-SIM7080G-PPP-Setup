import serial
import time
import config

# シリアルポートの設定
BAUD_RATE = 9600     # ボーレートをモデムに合わせて変更
ser = serial.Serial(config.PORT, BAUD_RATE)
ser.flushInput()
# 初期化処理


def send_at_command(command, wait_for_response=True):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode()
    if not bool(response):
        return send_at_command(command, wait_for_response)
    print(f"Response: {response}")
    return response

# モデムの設定


def initialize_modem():
    # send_at_command('AT')  # モデムの応答確認
    # send_at_command('AT+CPIN?')  # SIMカードのPIN確認
    # send_at_command('AT+CSQ')  # 信号強度確認
    # send_at_command('AT+CGATT?')  # ネットワーク接続状態確認
    # send_at_command('AT+COPS?')  # キャリア情報確認
    # send_at_command('AT+CGNAPN')  # APN情報確認（必要に応じて）
    # send_at_command('AT+CNCFG=0,1,"ppsim.jp"')  # APN設定
    # send_at_command('AT+CNACT=0,1')  # APN接続開始
    # send_at_command('ATD*99#')  # APN接続開始
    send_at_command("ATZ")  # モデムのリセット
    send_at_command("ATDT*99#")  #

# PPP接続を開始


def main():
    initialize_modem()  # モデムの設定と確認


if __name__ == "__main__":
    main()
    ser.close()
