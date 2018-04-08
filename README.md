# pycall
Simple test tool for API calling.

(python 3)

Can:
  - Load a text file and return the API response from each url in this file
  - Wait between requests
  - Print json response
  - Run in non-interactive mode with the config.json file

# Example:

# Interactive:

$ python3 pycall.py 
Time between requests in seconds: 3
Url file (one address per line): test

	Requesting - https://bitcoinfees.earn.com/api/v1/fees/recommended

<Response [200]>

3 properties received.

{
    "fastestFee": 10,
    "halfHourFee": 10,
    "hourFee": 10
}

Ended.

# Non-interactive

$ echo {"enabled": "yes","file": "test","wait": "5"} > config.json

$ python3 pycall.py >> output.txt

# Inside output.txt

Running in non-interactive mode...

	Requesting - https://bitcoinfees.earn.com/api/v1/fees/recommended

<Response [200]>

3 properties received.

{
    "fastestFee": 10,
    "halfHourFee": 10,
    "hourFee": 10
}

Ended.
