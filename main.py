from core.engine import Engine
from core.ui import banner

def main():
    banner()

    engine = Engine()

    print("Modules: net_scan, dns_probe")
    module = input("Select module: ")
    target = input("Target: ")

    engine.load(module)
    result = engine.run(module, target)

    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()
