import sys
import time

def banner():
    text = "VAULT STRATUM"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n" + "="*40)

def loading(msg):
    for i in range(3):
        print(f"{msg}{'.'*i}", end="\r")
        time.sleep(0.3)
