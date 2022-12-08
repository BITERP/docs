from datetime import datetime
import socket
#from PIL import Image
from time import sleep


camera_ip = '192.168.217.42'
tcp_send_port = 2001
tcp_receive_port = 2002
udp_listen_port = 6000

tcp_connection_1=socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)
tcp_connection_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  

tcp_connection_2=socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)
tcp_connection_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1) 

udp_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_DGRAM
)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1) 
 
def read_until(connection,waiting_bytes):
    waiting_len = len(waiting_bytes)
    recieve_len = waiting_len
    rcv_bytes = b''
    while True:
        rcv_bytes = rcv_bytes+connection.recv(recieve_len)
        recieve_len = 1
        if rcv_bytes[-waiting_len:] == waiting_bytes:
            return rcv_bytes

def test_send_receive(send_connection, recieve_connection):
    while True:
        start_readig = datetime.now()
        send_connection.sendall(b'TON')
        read_result = read_until(recieve_connection,b'\x0A')
        result_received = datetime.now()
        print(f"|| {result_received-start_readig} | {read_result} ||")

def same_connection():
    tcp_connection_1.connect((camera_ip,2001))
    test_send_receive(tcp_connection_1,tcp_connection_1)


def different_connection():
    tcp_connection_1.connect((camera_ip,2001))
    tcp_connection_2.connect((camera_ip,2002))
    test_send_receive(tcp_connection_1,tcp_connection_2)
  
def udp_receive():
    tcp_connection_1.connect((camera_ip,2001))
    udp_socket.bind(('0.0.0.0',6000))
    while True:
        start_readig = datetime.now()
        tcp_connection_1.sendall(b'TON')
        rcv_bytes = b''
        rcv_bytes = udp_socket.recvfrom(1024)
        result_received = datetime.now()
        print(f"|| {result_received-start_readig} | {rcv_bytes} ||")
        
if __name__ == "__main__":
    same_connection()
    #different_connection()
    #udp_receive()