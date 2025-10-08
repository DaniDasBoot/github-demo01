# SAFE ALTERNATIVE - Use JSON instead of pickle
import json
def load_user_data(data):
    return json.loads(base64.b64decode(data).decode('utf-8'))
