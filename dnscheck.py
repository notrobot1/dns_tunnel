import socket, binascii
def send_udp_message(message, address, port):
 message = message.replace(" ", "").replace("\n", "")
 server_address = (address, port)
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 try:
  sock.sendto(binascii.unhexlify(message), server_address)
  data, _ = sock.recvfrom(4096)
 finally:
  sock.close()
 return binascii.hexlify(data).decode("utf-8")
message = "AA AA 01 00 00 01 00 00 00 00 00 00 " + "07 65 78 61 6d 70 6c 65 03 63 6f 6d" +" 00 00 01 00 01"
response = send_udp_message(message, "8.8.8.8", 53)
print(response)
