import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    s = socket.socket()
    s.settimeout(0.3)
    try:
        s.connect((target, port))
        return port
    except:
        return None
    finally:
        s.close()

def run(target):
    ports = range(1, 1000)
    open_ports = []

    with ThreadPoolExecutor(max_workers=200) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)

    for r in results:
        if r:
            open_ports.append(r)

    return open_ports
