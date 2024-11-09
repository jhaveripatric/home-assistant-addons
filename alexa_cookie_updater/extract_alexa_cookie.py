import pickle
import json
import os

# Log all environment variables to check if PICKLE_FILE_NAME is set
print("All environment variables:", flush=True)
for key, value in os.environ.items():
    print(f"{key}: {value}", flush=True)

# Retrieve the pickle file name from the environment variable
pickle_file_name = os.getenv('PICKLE_FILE_NAME', 'alexa_media.default.pickle')

# Log the retrieved environment variable
print(f"Retrieved PICKLE_FILE_NAME from environment: {pickle_file_name}", flush=True)

# Set the paths for the .pickle and JSON files
pickle_file = f'/config/.storage/{pickle_file_name}'
json_file = '/config/node-red/alexa-cookie.json'

# Start of the script
print("Starting Alexa Cookie Updater script...", flush=True)

# Log the paths being used
print(f"Expected pickle file path: {pickle_file}", flush=True)
print(f"Output JSON file path: {json_file}", flush=True)

# Check if the .pickle file exists
if os.path.exists(pickle_file):
    print("Pickle file found. Attempting to open and load the file...", flush=True)
    with open(pickle_file, 'rb') as pf:
        try:
            # Attempt to load data from the pickle file
            data = pickle.load(pf)
            print("Pickle file loaded successfully.", flush=True)

            # Extract the 'cookies' field if it exists
            if 'cookies' in data:
                cookie_data = data['cookies']
                print("Cookies field found in pickle data.", flush=True)
            else:
                cookie_data = {}
                print("Cookies field not found in pickle data. Using empty dictionary.", flush=True)

            # Attempt to write cookie data to JSON file
            print("Saving cookie data to JSON file...", flush=True)
            with open(json_file, 'w') as jf:
                json.dump(cookie_data, jf)
            print("Cookie data saved to JSON successfully.", flush=True)

        except Exception as e:
            print(f"Error while loading pickle data: {e}", flush=True)
else:
    print("Pickle file not found. Please check the file path and ensure the file exists.", flush=True)
