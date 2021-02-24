from socket import *
import binascii
import base64
import requests
host = "IP"
port = 53

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def getRequest(url):
   full_page = requests.get(url, headers=headers).text
   return full_page


addr = (host, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)
while True:
 conn, addr = udp_socket.recvfrom(1024)
 
 url = str(conn)[50:][:-21] #выдернуть запрос
 message_bytes = base64.b64decode(url)
 ok = message_bytes.decode('utf-8')
 #вызвать функцию гет запроса

 base =  base64.b64encode(getRequest(ok).encode('UTF-8')) #закодировать в бэйс ответ сервера
 n = 256
 spl = [base[i:i+n] for i in range(0, len(base), n)]
 print(spl)

 for i in spl:
  send = " ".join("{:02x}".format(ord(c)) for c in i.decode("UTF-8")).replace(" ", "").replace("\n", "")
  print(send)
 #base to hex 
  udp_socket.sendto(binascii.unhexlify("aaaa85800001000100000000076578616d706c6503636f6d0000010001c00c00010001000000000004"+send), addr)
 udp_socket.sendto(binascii.unhexlify("ffffff"), addr)
