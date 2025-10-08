'''
# test_vuln.py - clearly marked test file
import pickle
import base64

# INTENTIONAL TEST VULNERABILITY - DO NOT USE IN PRODUCTION
def load_user_data(data):
    return pickle.loads(base64.b64decode(data))

#Update to file 5
'''
