import socket

UDP_IP = ""
UDP_PORT = 53533
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(2048)
    # buffer size is 2048 bytes
    print("received message: %s" % data)
    data = data.decode()
    param = data.split('\n')
    for i in param:
        name, val = i.split('=')
        if name == 'NAME':
            hostname = val
        if name == 'VALUE':
            ip = val
    # if register
    if len(param) > 2:
        with open('domain.txt', 'a+') as f:
            f.write(data)
        # send back message
        sock.sendto("registration succeeds".encode(), addr)
    # if query
    elif len(param) == 2:
        # format is correct
        if 'TYPE' in data and 'NAME' in data:
            with open('domain.txt', 'r') as f:
                for line in f:
                    if hostname in line:
                        ip_val = f.readline()
                        ip = ip_val.split('=')[1]
                        break
                # send back message
                msg = "TYPE=A\n" + "NAME=" + hostname + "\nVALUE=" + ip + "\nTTL=10"
                sock.sendto(msg.encode(), addr)

    else:
        # return wrong format message
        sock.sendto("wrong format".encode(), addr)




