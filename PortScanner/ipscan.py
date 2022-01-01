import portscanner

ip = 'testphp.vulnweb.com'
port_num = 500
timeout = 0.5

portscanner.scan(ip,port_num,timeout)