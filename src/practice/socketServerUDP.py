
import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))


    print("Server Started.")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("message From: " + str(addr))
        print("from connected user: " + data)
        data = data.upper()
        print("sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    s.close()

if __name__ == '__main__':
    Main()
    
