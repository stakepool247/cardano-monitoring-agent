from time import sleep
from prometheus_api_client import PrometheusConnect
from .args import args
from .config import config
from .fetcher import Fetcher
from .sender import Sender

def main():
    fetcher = Fetcher()
    sender = Sender()

    metrics = fetcher.gather_config_metrics('node:metrics')
    if metrics is not None and len(metrics) > 0:
        result = sender.send_metrics(metrics)
        print(result)
    

if __name__ == '__main__':
    main()
