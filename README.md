
---

# D-TECH Terminal Tools

## Overview

D-TECH Terminal Tools is a collection of command-line utilities that provide features such as domain lookups, HTTP header analysis, SQL injection testing, and more, all presented in a futuristic, hacker-themed interface.

## Features

- **Get IP Address of a Domain**
- **Get HTTP Headers**
- **SQL Injection Test**
- **Subdomain Enumeration**
- **Crack Hashes (John the Ripper)**
- **Search Exploits (Searchsploit)**
- **Whois Lookup**
- **SSL/TLS Certificate Inspection**
- **XSS Testing**

## Requirements

Before running the tool, you need to install the following dependencies.

### System Update & Upgrade

1. **Update and upgrade your system**:
   ```bash
   apt update
   apt upgrade
   ```

### Packages

2. **Install required Python packages**:
   ```bash
   apt install python3-pip
   pip3 install requests whois sublist3r termcolor
   ```

3. **Install additional tools**:
   - **John the Ripper**:
     ```bash
     apt install john
     ```
   - **Searchsploit** (part of Exploit-DB):
     ```bash
     apt install exploitdb
     ```

### SSL/TLS Library

`ssl` is part of Python’s standard library, so no installation is required.

## Usage

Once all dependencies are installed, follow the steps below to run the tool.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Preasx24/D-TECH_terminal_tools.git
   cd D-TECH_terminal_tools
   ```

2. **Execute the Tool**:
   ```bash
   python3 dtech_tool.py
   ```

## Example Usage

Here’s how you can use one of the features:

- To get the IP address of a domain:
  ```bash
  Choose a tool to use:
  [1] Get IP Address of a Domain
  Enter the domain: example.com
  ```

## Contributing

You are welcome to contribute by forking the repository, making changes, and submitting pull requests. If you encounter any issues or have feature requests, please open an issue on the [GitHub repository](https://github.com/Preasx24/D-TECH_terminal_tools/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

