# test_vuln.py - clearly marked test file
import pickle
import base64

# INTENTIONAL TEST VULNERABILITY - DO NOT USE IN PRODUCTION
def load_user_data(data):
    return pickle.loads(base64.b64decode(data))

# Adding an arbitrary comment.
# Second arbitrary comment.
# Third arbitrary comment.

'''

import json
import base64

def load_user_data(data):
    try:
        decoded = base64.b64decode(data).decode('utf-8')
        parsed = json.loads(decoded)
        # Add schema validation here
        return parsed
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f"Invalid data format: {e}")
'''
