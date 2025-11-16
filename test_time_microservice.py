"""
Time Microservice Test Program
A test program that tests all three endpoints and shows the responses
"""

import requests
import json

print("\n--- TEST 1: Get Military Time ---")
response = requests.get('http://localhost:3000/time/military')
data = response.json()
print(data['military_time'])
print("Full response:", json.dumps(data, indent=2))

print("\n--- TEST 2: Get Current UTC Time ---")
response = requests.get('http://localhost:3000/time/current')
data = response.json()
print("Status Code:", response.status_code)
print("Response:", json.dumps(data, indent=2))

print("\n--- TEST 3: Get Time in New York ---")
response = requests.get('http://localhost:3000/time/timezone?timezone=America/New_York')
data = response.json()
print("Status Code:", response.status_code)
print("Response:", json.dumps(data, indent=2))

print("\n--- TEST 4: Get Time in Los Angeles ---")
response = requests.get('http://localhost:3000/time/timezone?timezone=America/Los_Angeles')
data = response.json()
print("Response:", json.dumps(data, indent=2))

print("\n--- TEST 5: Test Error Handling (Invalid Timezone) ---")
response = requests.get('http://localhost:3000/time/timezone?timezone=Invalid/Timezone')
data = response.json()
print("Status Code:", response.status_code)
print("Response:", json.dumps(data, indent=2))

print("\n--- All tests are complete! ---")
