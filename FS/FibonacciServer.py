from flask import Flask, request, Response
import json
import socket

app = Flask(__name__)


@app.route('/register', methods=['PUT'])
def register():
    info = json.loads(request.data.decode())
    as_ip = info['as_ip']
    as_port = info['as_port']
    hostname = info['hostname']
    ip = info['ip']
    # send to AS server to register
    msg = ["TYPE=A", "NAME="+hostname, "VALUE="+ip, "TTL=10"]
    parsed_msg = "\n".join(msg)
    fib_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fib_socket.sendto(parsed_msg.encode(), (as_ip, 53533))
    response = fib_socket.recv(2048)
    if response.decode() == 'registration succeeds':
        return Response('Registration Success', 201)


@app.route('/fibonacci/<number>', methods=['GET'])
def fibonacci(number):
    try:
        num = int(number)
        return str(Fibonacci_cal(num)), 200
    except:
        return Response('Bad format', 400)


def Fibonacci_cal(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci_cal(n - 1) + Fibonacci_cal(n - 2)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)
