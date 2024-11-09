import pickle
import json
import os

# Retrieve the pickle file name from the environment variable
pickle_file_name = os.getenv('PICKLE_FILE_NAME', 'alexa_media.default.pickle')  # Default if not set
pickle_file = f'/config/.storage/{pickle_file_name}'
json_file = '/config/node-red/alexa-cookie.json'

# Check if the .pickle file exists
if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as pf:
        try:
            # Load the pickle data
            data = pickle.load(pf)
            # Extract the 'cookies' field (if it exists)
            cookie_data = data.get('cookies', {})

            # Save cookie data to JSON file
            with open(json_file, 'w') as jf:
                json.dump(cookie_data, jf)
            print("Cookie data saved to JSON.")
        except Exception as e:
            print(f"Error reading pickle file: {e}")
else:
    print("Pickle file not found.")
