import pickle
import json
import os

# Log all environment variables to check if PICKLE_FILE_NAME is set
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Retrieve the pickle file name from the environment variable
pickle_file_name = os.getenv('PICKLE_FILE_NAME', 'alexa_media.default.pickle')  # Default if not set

# Log the retrieved environment variable
print(f"Retrieved PICKLE_FILE_NAME from environment: {pickle_file_name}")

# Set the paths for the .pickle and JSON files
pickle_file = f'/config/.storage/{pickle_file_name}'
json_file = '/config/node-red/alexa-cookie.json'

# Start of the script
print("Starting Alexa Cookie Updater script...")

# Log the paths being used
print(f"Expected pickle file path: {pickle_file}")
print(f"Output JSON file path: {json_file}")

# Check if the .pickle file exists
if os.path.exists(pickle_file):
    print("Pickle file found. Attempting to open and load the file...")
    with open(pickle_file, 'rb') as pf:
        try:
            # Attempt to load data from the pickle file
            data = pickle.load(pf)
            print("Pickle file loaded successfully.")

            # Extract the 'cookies' field if it exists
            if 'cookies' in data:
                cookie_data = data['cookies']
                print("Cookies field found in pickle data.")
            else:
                cookie_data = {}
                print("Cookies field not found in pickle data. Using empty dictionary.")

            # Attempt to write cookie data to JSON file
            print("Saving cookie data to JSON file...")
            with open(json_file, 'w') as jf:
                json.dump(cookie_data, jf)
            print("Cookie data saved to JSON successfully.")

        except Exception as e:
            print(f"Error while loading pickle data: {e}")
else:
    print("Pickle file not found. Please check the file path and ensure the file exists.")
