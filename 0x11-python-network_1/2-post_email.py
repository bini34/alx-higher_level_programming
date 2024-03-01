#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a
parameter, and displays the body of the response
(decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    with urllib.request.urlopen(sys.argv[1], data=data) as res:
        email = res.read().decode('utf-8')
        print(f"Your email is: {email}")
