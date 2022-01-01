import socket
from IPy import IP


def scan(target, port_num, timeout):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target]' + str(target))
    for port in range(1,port_num):
        scan_port(converted_ip, port, float(timeout))


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port' + str(port))
    except:
        # print('[-] Port '+ str(port) +' is Closed')
        pass

if __name__ == "__main__":
    targets = input('[+] Enter Target/s to Scan: (split multiple targets with ,): ')
    port_num = input('Enter Number of Ports That You Want To Scan: ')
    timeout = input('Enter timeout in seconds: ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '),int(port_num),float(timeout))
    else:
        scan(targets, int(port_num), float(timeout))