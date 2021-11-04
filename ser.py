import serial
import time
import datetime
import sys
import threading
import getpass

class pclr:
    BLACK   = '\u001b[30m'
    RED     = '\u001b[31m'
    GREEN   = '\u001b[32m'
    YELLOW  = '\u001b[33m'
    BLUE    = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN    = '\u001b[36m'
    WHITE   = '\u001b[37m'
    
    NORMAL   = '\u001b[0m'

if len(sys.argv) >= 3:
    port = sys.argv[1]
    baud = int(sys.argv[2])
else:
    port = input('Enter COM port: ')
    baud = input('Enter BAUD rate: ')
line_ending = '\n'
if len(sys.argv) == 4:
    if sys.argv[3].lower() == 'lf':
        line_ending = b'\n'
    if sys.argv[3].lower() == 'cr':
        line_ending = b'\r'
    if sys.argv[3].lower() == 'crlf':
        line_ending = b'\r\n'
    

serial_opened = True
def open_ser():
    return serial.Serial(port, baudrate=baud, timeout=0)

rotator = '\\|/-'
print(f"{pclr.YELLOW}CONNECTING{pclr.NORMAL}")
rotator_i = 0
while True:
    try:
        ser = open_ser()
        break
    except:
        print(f"{pclr.YELLOW}{rotator[rotator_i%len(rotator)]}\b{pclr.NORMAL}", end='', flush=True)
        rotator_i += 1
        time.sleep(1)
print(f" \n{pclr.GREEN}CONNECTED{pclr.NORMAL}")

input = ''
def read_input():
    global input
    global ser
    global serial_opened
    while True:
        get = getpass.getpass(prompt='')
        input=f'{input}{get}'
        if len(input)>0:
            color = pclr.BLUE if serial_opened else pclr.RED
            print(f"{color}{input}{pclr.NORMAL}")
            if serial_opened:
                try:
                    ser.write(input.encode('utf-8'))
                    ser.write(line_ending)
                except:
                    print(f"{pclr.RED}Unable to write{pclr.NORMAL}")
            input = ''

read_input_thread = threading.Thread(target=read_input)
read_input_thread.daemon = True
read_input_thread.start()

while True:
    if not read_input_thread.is_alive():
        exit()
    try:
        if ser.in_waiting > 0:
            try:
                in_char = ser.read().decode('utf-8')
                print(in_char, end='', flush=True)
                with open('masterlog.log', 'a') as f:
                    print(in_char, end='', flush=True,  file=f)
                    if in_char == '\n':
                        print(f'{port} {baud} {datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")} >', end='', flush=True,  file=f)
            except UnicodeDecodeError:
                pass
    except serial.serialutil.SerialException:
        if serial_opened:
            print(f"{pclr.RED}DISCONNECTED{pclr.NORMAL}")
            serial_opened = False
        time.sleep(2)
        try:
            ser = open_ser()
            print(f"{pclr.GREEN}RECONNECTED{pclr.NORMAL}")
            serial_opened = True
        except serial.serialutil.SerialException:
            pass
