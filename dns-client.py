import binascii
import socket
import base64
from sys import argv
s = "https://docs.python.org/3/library/ssl.html"
s = argv
print(s)
base64_url = base64.b64encode(s[1].encode('UTF-8'))
arr = []
test = ""
url = " ".join("{:02x}".format(ord(c)) for c in base64_url.decode("UTF-8"))

def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        while True:
         data, _ = sock.recvfrom(4096)
         ss = binascii.hexlify(data).decode("utf-8")
         sss = ss[82:]
         global test
         test = test+sss
         if ss == "ffffff":
          break

    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)


message = "AA AA 01 00 00 01 00 00 00 00 00 00 " + url +" 00 00 01 00 01"

response = send_udp_message(message, "iP", 53)
#print(format_hex(response))
#print(response)
format_hex(response)
#print(test.decode("hex"))
base = bytearray.fromhex(test).decode()
end = base64.b64decode(base.encode())


 #f.write(index)
print(str(end).replace("\r","").replace("\n",""))
