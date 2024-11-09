# Alexa Cookie Updater

The **Alexa Cookie Updater** is a custom Home Assistant add-on that extracts and saves Alexa cookie data for use in Node-RED. This add-on reads the Alexa Media Player `.pickle` session file, extracts the cookie, and saves it to a JSON file that can be accessed by Node-RED to keep Alexa functionality synced.

## Features
- Periodically extracts the Alexa cookie from the `.pickle` file.
- Saves the cookie in JSON format for Node-RED integration.
- Configurable `.pickle` file name to protect sensitive information.

## Installation

### Step 1: Clone the Repository
1. Clone this repository to your Home Assistant add-ons directory or add it as a custom repository in Home Assistant.

### Step 2: Configure the Add-On
1. Go to **Settings > Add-ons** in Home Assistant.
2. Add this repository as a custom add-on repository.
3. Install the `Alexa Cookie Updater` add-on.

### Step 3: Configure the Pickle File Name
1. In the add-on configuration, enter the name of your Alexa Media Player `.pickle` file (e.g., `alexa_media.YOUR_EMAIL.pickle`) under `pickle_file_name`.
    - **Note:** This value is securely stored and not hardcoded in the codebase.

### Step 4: Run the Add-On
1. Start the add-on to generate the JSON cookie file.
2. Optionally, set up a Home Assistant automation to run the add-on periodically (e.g., every 6 hours) to keep the cookie up-to-date.

## Automation Example

To automate the add-on execution every 6 hours:
```yaml
- alias: "Run Alexa Cookie Updater Add-On"
  trigger:
    - platform: time_pattern
      hours: "/6"
  action:
    - service: hassio.addon_start
      data:
        addon: local_alexa_cookie_updater
