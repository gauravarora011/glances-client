import socket
import psutil
import time

def onbutton_click(client_name):
    s = socket.socket()
    host = "192.168.0.2"
    port = 12348
    #print(psutil.disk_usage('/').percent)
    s.connect((host, port))
    print s.recv(1024)
    s.send(client_name)
    time.sleep(1)
    while True:
        cpu = str(len(psutil.pids()))
        cpu2 = str(psutil.cpu_percent())
        mem = str(psutil.virtual_memory().percent)
        disk = str(psutil.disk_usage('/').percent)
        message = cpu + " " + cpu2 + " "+ mem + " " + disk
        s.send(message)
        time.sleep(2)
    s.close