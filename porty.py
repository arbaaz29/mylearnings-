import socket
import termcolor
def scan(ip,ports):
    print(termcolor.colored((f'\nScannig for target {ip}!\n'), 'green'))
    for port in range(1,ports):
        scan_port(ip,port)
def scan_port(ip, portt):
    try:
        s= socket.socket()
        s.connect((ip,portt))
        print(f'port number {portt} is open!')
        s.close()
    except:
        pass
targs=input("Enter the target you want to scan (if multiple use comma',' to seprate them)!: ")
portt=int(input("Enter the number of ports you want to scan!: "))
if ',' in targs:
    for ip in targs.split(','):
        scan(ip.strip(' '),portt)
else:
    scan(targs,portt)
