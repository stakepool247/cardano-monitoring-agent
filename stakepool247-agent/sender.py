from typing import Dict
from requests import post
from datetime import datetime
from .config import config

class Sender():

    def __init__(self):
        self.api_url = config['api']['api_metrics_url']
        self.device_key = config['api']['device_key']
    
    def send_metrics(self, metrics: Dict[str, float]) -> bool:
        response = post(self.api_url, headers={
            'Authorization': 'Bearer {0}'.format(self.device_key)
        }, json={
            'time': datetime.now().isoformat(),
            'metrics': metrics
        })

        if response.status_code == 200:
            return True
        return False