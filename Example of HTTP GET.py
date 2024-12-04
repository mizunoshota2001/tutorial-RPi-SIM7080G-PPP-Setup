import serial
import time
import config
# シリアルポートの設定
ser = serial.Serial(config.PORT, 9600)

# 初期化処理


def send_at_command(command, wait_for_response=True):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode()
    if not bool(response):
        return send_at_command(command, wait_for_response)
    print(f"Response: {response}")
    return response


send_at_command('AT+SHCONF="URL","http://httpbin.org"')
send_at_command('AT+SHCONF="BODYLEN",1024')
send_at_command('AT+SHCONF="HEADERLEN",350')
send_at_command('AT+SHCONN')
send_at_command('AT+SHSTATE?')
send_at_command('AT+SHCHEAD')
send_at_command('AT+SHAHEAD="User-Agent","curl/7.47.0"')
send_at_command('AT+SHAHEAD="Cache-control","no-cache"')
send_at_command('AT+SHAHEAD="Connection","keep-alive"')
send_at_command('AT+SHAHEAD="Accept","*/*"')
send_at_command('AT+SHREQ="/get?user=jack&password=123",1')
time.sleep(5)
send_at_command('AT+SHREAD=0,384')
send_at_command('AT+SHDISC')

# 終了処理
ser.close()
