from flask import Flask, request, Response
import requests
import socket

app = Flask(__name__)


@app.route('/')
def initialize():
    return "You should visit /fibonacci with several parameters to obtain the IP address of the Fibonacci Server"

@app.route('/fibonacci')
def fibonacci():
    hostname = request.args.get('hostname', None)
    fs_port = request.args.get('fs_port', None)
    number = request.args.get('number', None)
    as_ip = request.args.get('as_ip', None)
    as_port = request.args.get('as_port', None)
    if any([hostname, fs_port, number, as_ip, as_port]) is None:
        return Response("Bad Request", 404)
    else:
        # retrieve FS ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = "TYPE=A\n"+"NAME="+hostname
        sock.sendto(msg.encode(), (as_ip, int(as_port)))
        response, addr = sock.recvfrom(2048)
        info = response.decode().split('\n')
        print(info)
        ip = info[2].split('=')[1]
        fibonacci_query = f"http://{ip}:{fs_port}/fibonacci/{number}"
        response = requests.get(fibonacci_query,)
        if response.status_code == 200:
            return response.text, 200


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
