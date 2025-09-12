import json
import requests
import sys

# One argument is required when running the program
# If that argument is not provided, exit program
if len(sys.argv) != 2:
    sys.exit()


# Request data from the itunes api
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# Format and print data
# print(json.dumps(response.json(), indent=2))

# Convert the response into json
output = response.json()
# Go through each song received in the response
for result in output["results"]:
    # Display only the name of the track(s)
    print(result["trackName"])