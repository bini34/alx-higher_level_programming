#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It also handles urllib.error.HTTPError exceptions.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Send the request
        with urllib.request.urlopen(url) as response:
            # Display the body of the response
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")
