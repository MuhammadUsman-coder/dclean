#!/usr/bin/env python3
import sys
import re

def load_tld_list(file_path="tlds.txt"):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        sys.exit(1)

def is_domain_valid(domain):
    tld_list = load_tld_list()

    if not isinstance(domain, str):
        return False

    domain = domain.lower()

    if not domain or len(domain) < 1 or len(domain) > 253:
        return False

    labels = domain.split(".")
    if len(labels) < 2:
        return False

    for label in labels:
        if len(label) > 63 or re.search(r"[^a-zA-Z0-9\-_]", label):
            return False
        if label.startswith("-") or label.endswith("-") or "--" in label:
            return False
        if "xn--" in label and not label.startswith("xn--"):
            return False

    tld = labels[-1]
    if tld not in tld_list:
        return False

    return True

if __name__ == "__main__":
    for line in sys.stdin:
        domain = line.strip()
        if is_domain_valid(domain):
            print(domain)
