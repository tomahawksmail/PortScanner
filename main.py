import socket

ip = '185.132.1.134'
def scan_port(ip,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip,port))
     print('Port :',port,' its open.')
     connect.close()
  except:
     print(i, 'close')
for i in range(0, 65000):
# i = 55636

    scan_port(ip, i)
