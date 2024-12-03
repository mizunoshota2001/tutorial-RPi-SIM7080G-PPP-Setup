import serial
import time

# シリアルポートの設定
ser = serial.Serial('COM5', 9600)

# 初期化処理
def send_at_command(command, wait_for_response=True):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode()
    if not bool(response):
        return send_at_command(command, wait_for_response)
    print(f"Response: {response}")
    return response

send_at_command('AT+CPIN?')
send_at_command('AT+CSQ')
send_at_command('AT+CGATT?')
send_at_command('AT+COPS?')
send_at_command('AT+CGNAPN')
send_at_command('AT+CNCFG=0,1,"ppsim.jp"')
send_at_command('AT+CNACT?')

# 終了処理
ser.close()
