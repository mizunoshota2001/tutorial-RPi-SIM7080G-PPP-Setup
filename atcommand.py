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

send_at_command('AT')
send_at_command('AT+CPIN?')
send_at_command('AT+CNMP=38')
send_at_command('AT+CMNB=1')
send_at_command('AT+CSQ')
send_at_command('AT+CGREG?')
send_at_command('AT+CGNAPN')
send_at_command('AT+CPSI?')
send_at_command('AT+CNACT=0,1')
send_at_command('AT+CNACT?')
send_at_command('AT+CNCAT=0,0')

# 終了処理
ser.close()
