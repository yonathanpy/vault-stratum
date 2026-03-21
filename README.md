<p align="center">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAMAAAC5zwqKAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAAd0SU1FB+YJEg4bJIkxWT0AAAGHSURBVHja7dQxDoIwEATQvP//9PyG0UjQG8xvIDnZGx2Uh2QX8pARCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJ+S+4+v0zuvpOFKdmo+3XRkl6dnZ0o7enp6RlN5+fna/2JV944vvuUfXz8/Nzp7e3u429vZ2TEj8qM+UXl5cvn379nZvbm4+fPny8W3t7fTM/OUlJSY2NjRUVFBoaGgODg4LCwsMDIyAiAgIAAAAPDw8fHx8+Pj4eHh4QEBAT///wAAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAAA+AOkcAPz//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAAAAD+AAHFDNXCAAAAAElFTkSuQmCC" width="400" alt="Vault Stratum Banner" />
</p>

# VAULT‑STRATUM

Modular reconnaissance and execution framework designed for controlled security research and network analysis.

---

## Overview

VAULT-STRATUM is a lightweight, extensible framework built around a dynamic module loader. It enables structured execution of reconnaissance tasks such as port scanning and DNS probing through a unified interface.

The architecture emphasizes clarity, modularity, and rapid extension.

---

## Features

* Dynamic module loading
* Multi-threaded network scanning
* DNS enumeration module
* Clean separation between core engine and modules
* Minimal dependencies

---

## Project Structure

```
vault-stratum/
├── core/
│   ├── engine.py
│   ├── ui.py
├── modules/
│   ├── net_scan.py
│   ├── dns_probe.py
├── main.py
├── requirements.txt
```

---

## Modules

### net_scan

Performs threaded TCP port scanning across a defined port range.

### dns_probe

Enumerates common subdomains and resolves them.

---

## Usage

```
python main.py
```

Then:

```
Select module: net_scan
Target: 192.168.1.1
```

or

```
Select module: dns_probe
Target: example.com
```

---

## Design Philosophy

* Minimal surface complexity
* High readability
* Expandable module system

---

## Future Work

* Plugin auto-discovery
* Config-based scanning profiles
* Output formatting (JSON / logs)
* Integration with additional enumeration modules

---

