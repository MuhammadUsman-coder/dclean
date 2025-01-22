# dclean
A simple domain cleaning tool removing garbage and invalid domains.

# Rules
- Length should be > 1 and < 253.
- Should have at least 1 dot.
- Can only contain a-z A-Z 0-9 - . and _
- Any single part of domain cannot contain more than 63 characters.
- Cannot start or end with - hyphen.
- Cannot contain two consecutive hyphens -- anywhere except if it starts with xn--
- Should end with a valid tld.

# Valid subs
```
example.com
sub.example.com
exa-mple.com
exa_mple.com
xn--c1yn36f.com
```

# Invalid Subs
```
123
123.123
example
-example.com
example-.com
exa--mple.com
example.doesnotexist
xn--c1yn--bb.com
*.com
example.*.com
```
# Usage
cat subs| ./dclean
