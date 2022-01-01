import socket
from IPy import IP

class PortScan():
    banners = []
    open_ports = []
    def __init__(self, target, port_num, timeout):
        self.target = target
        self.port_num = port_num
        self.timeout = timeout

    def scan(self):
        for port in range(1,self.port_num):
            self.scan_port(port, self.timeout)


    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self,port, timeout):
        try:
            converted_ip = self.check_ip(self.target)
            sock = socket.socket()
            sock.settimeout(timeout)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass