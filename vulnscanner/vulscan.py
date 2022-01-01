import portscanner

targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
port_num = int(input('[+] * Enter Number of Ports That You Want To Scan: '))
timeout = float(input('[+] * Enter timeout in seconds: '))

vul_file = input("[+] * Enter Path To The File With Vulnerable Softwares: ")
print('\n')

target = portscanner.PortScan(targets_ip,port_num,timeout)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
        count+=1