<p align="center">
  <img src="https://img.icons8.com/ios-filled/500/000000/database.png" width="200" alt="VAULT-STRATUM Database Icon"/>
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

