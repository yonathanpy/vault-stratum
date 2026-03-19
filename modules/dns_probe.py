import socket

def run(domain):
    subs = ["www","mail","api","dev","test","vpn"]
    found = []

    for s in subs:
        try:
            ip = socket.gethostbyname(f"{s}.{domain}")
            found.append((s, ip))
        except:
            pass

    return found
