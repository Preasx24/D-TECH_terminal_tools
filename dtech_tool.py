# Save the following Python script as dtech_tool.py

import time
import socket
import requests
import os
import whois
import ssl
import sublist3r
from termcolor import colored

# Fancy D-TECH loading screen
def dtech_loading():
    print(colored("\n[Initializing D-TECH system...]", 'cyan'), flush=True)
    time.sleep(2)
    print(colored("[Loading core modules...]", 'cyan'), flush=True)
    time.sleep(2)
    print(colored("[Connecting to the network...]", 'cyan'), flush=True)
    time.sleep(2)
    print(colored("[Updating libraries...]", 'cyan'), flush=True)
    time.sleep(2)
    print(colored("[D-TECH Systems Ready]\n", 'green'), flush=True)
    time.sleep(1)

# Menu for selecting the tool
def display_menu():
    print(colored("\n********** D-TECH TOOLS MENU **********", 'magenta'))
    print(colored("[1] Get IP Address of a Domain", 'yellow'))
    print(colored("[2] Get HTTP Headers", 'yellow'))
    print(colored("[3] SQL Injection Test", 'yellow'))
    print(colored("[4] Subdomain Enumeration", 'yellow'))
    print(colored("[5] Crack Hashes (John the Ripper)", 'yellow'))
    print(colored("[6] Search Exploits (Searchsploit)", 'yellow'))
    print(colored("[7] Whois Lookup", 'yellow'))
    print(colored("[8] SSL/TLS Certificate Inspection", 'yellow'))
    print(colored("[9] XSS Testing", 'yellow'))
    print(colored("[0] Exit", 'red'))

    choice = input(colored("Enter your choice (0-9): ", 'cyan'))
    return choice

# Functions for each tool

def get_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip_address}")
    except socket.gaierror:
        print(f"Could not retrieve the IP address for {domain}")

def get_http_headers(url):
    try:
        response = requests.head(url)
        print(f"Headers for {url}:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve headers for {url}: {e}")

def sql_injection_test(url):
    payload = "' OR '1'='1"
    full_url = f"{url}?id={payload}"
    try:
        response = requests.get(full_url)
        if "sql" in response.text.lower() or "error" in response.text.lower():
            print(f"Possible SQL Injection vulnerability found at {url}")
        else:
            print(f"No SQL Injection vulnerability detected at {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def subdomain_enumeration(domain):
    subdomains = sublist3r.main(domain, 40, outputfile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
    print(f"Subdomains of {domain}:")
    for subdomain in subdomains:
        print(subdomain)

def crack_hash(hash_file):
    os.system(f"john {hash_file}")

def search_exploit(term):
    os.system(f"searchsploit {term}")

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"Failed to perform Whois lookup for {domain}: {e}")

def ssl_certificate(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            print(cert)

def xss_test(url):
    payload = "<script>alert('XSS');</script>"
    try:
        response = requests.get(url, params={'q': payload})
        if payload in response.text:
            print(f"Possible XSS vulnerability found at {url}")
        else:
            print(f"No XSS vulnerability detected at {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def run_dtech():
    dtech_loading()

    while True:
        choice = display_menu()

        if choice == '1':
            domain = input("Enter the domain: ")
            get_ip(domain)
        elif choice == '2':
            url = input("Enter the URL: ")
            get_http_headers(url)
        elif choice == '3':
            url = input("Enter the URL to test for SQL injection: ")
            sql_injection_test(url)
        elif choice == '4':
            domain = input("Enter the domain: ")
            subdomain_enumeration(domain)
        elif choice == '5':
            hash_file = input("Enter the path to the hash file: ")
            crack_hash(hash_file)
        elif choice == '6':
            term = input("Enter the search term (e.g., software name): ")
            search_exploit(term)
        elif choice == '7':
            domain = input("Enter the domain: ")
            whois_lookup(domain)
        elif choice == '8':
            domain = input("Enter the domain: ")
            ssl_certificate(domain)
        elif choice == '9':
            url = input("Enter the URL to test for XSS: ")
            xss_test(url)
        elif choice == '0':
            print(colored("\n[D-TECH system shutting down...]", 'red'))
            time.sleep(2)
            break
        else:
            print(colored("\nInvalid choice. Please try again.", 'red'))

if __name__ == "__main__":
    run_dtech()
