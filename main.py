import os
import socket


def get_dirlist():
    if os.path.isfile("index.html"):
        file = open('index.html')
        page = file.read()
    else:
        dirlist = os.listdir('.')
        links = ""
        for dir in dirlist:
            links +='<li><a href="#">{}</a></li>'.format(str(dir))
        page  = "<html><head></head><body><ul>{}</ul></body></html>".format(links)
    return page

data = get_dirlist()
HOST = ""
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)

print("Matrix on port {}".format(PORT) + ", CTRL-C to exit")

while True:
    c, (HOST, PORT) = s.accept()
    print ('Got connection from', HOST, PORT)

    c.recv(1000)
    c.send('HTTP/1.0 200 OK\n'.encode("utf-8"))
    c.send('Content-Type: text/html\n\n'.encode("utf-8"))
    c.send(data.encode("utf-8"))
    c.close()
