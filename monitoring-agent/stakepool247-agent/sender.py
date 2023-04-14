from email import header
from os import path
from typing import Dict
from requests import post, get
from datetime import datetime
from config import config

class Sender():

    def __init__(self):
        self.api_url = config['api']['api_metrics_url'].strip('"')
        self.device_key = config['api']['device_key'].strip('"')
        self.token_refresh_url = config['api']['api_token_refresh_url'].strip('"')
    
    def send_metric_request(self, metrics: Dict[str, float]) -> int:
        response = post(self.api_url, headers={
            'Authorization': 'Bearer {0}'.format(self.load_access_token())
        }, json={
            'time': datetime.now().isoformat(),
            'metrics': metrics
        })

        return response.status_code
    
    def refresh_token(self) -> bool:
        response = get(self.token_refresh_url, headers={
            'Authorization': 'Bearer {0}'.format(self.device_key)
        })
        if response.status_code != 200:
            return False
        access_token = response.json()['token']
        self.save_access_token(access_token)
        return True

    def send_metrics(self, metrics: Dict[str, float]) -> bool:
        metrics_response = self.send_metric_request(metrics)
        if metrics_response == 200:
            return True

        if metrics_response != 403:
            return False

        if self.refresh_token():
            metrics_response = self.send_metric_request(metrics)
            if metrics_response == 200:
                return True

        return False
    
    def token_file_path(self):
        return path.join(path.dirname(path.realpath(__file__)), 'token.txt')
    
    def save_access_token(self, token: str) -> None:
        with open(self.token_file_path(), 'w+') as f:
            f.write(token)
    
    def load_access_token(self) -> str:
        if path.exists(self.token_file_path()):
            with open(self.token_file_path(), 'r') as f:
                return f.read()
        return ''
