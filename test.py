import json
import os

def check_creds_file():
    # Check if the credentials file exists
    creds_file = 'creds.json'
    if not os.path.exists(creds_file):
        print(f"Error: Credentials file '{creds_file}' not found!")
        return False
    
    # Read credentials from JSON file
    try:
        with open(creds_file) as f:
            creds = json.load(f)
        
        # Print the credentials
        print(f"Found credentials file at: {os.path.abspath(creds_file)}")
        
        # Print the credentials
        client_id = creds.get("CLIENT_ID")
        client_secret = creds.get("CLIENT_SECRET")
        
        print(f"CLIENT_ID: {client_id}")
        print(f"CLIENT_SECRET: {client_secret[:4] + '...' if client_secret else None}")
        
        # Check if they exist
        if not client_id:
            print("Warning: CLIENT_ID is not set in creds.json file")
            
        if not client_secret:
            print("Warning: CLIENT_SECRET is not set in creds.json file")
            
        return True
    
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{creds_file}'")
        return False
    
    except Exception as e:
        print(f"Error reading credentials file: {e}")
        return False

if __name__ == "__main__":
    check_creds_file()