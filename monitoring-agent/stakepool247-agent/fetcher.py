from typing import Dict, Optional
from prometheus_api_client import PrometheusConnect
from .config import config

class Fetcher():

    def __init__(self):
        self.prometheus = PrometheusConnect(url = config['node']['prometheus_url'], disable_ssl=True)
    
    def get_metric_value(self, query: str) -> Optional[float]:
        metric = self.prometheus.custom_query(query)
        if len(metric) > 0 and 'value' in metric[0] and len(metric[0]['value']) > 1:
            try:
                return float(metric[0]['value'][1])
            except ValueError:
                return None
        return None

    def gather_config_metrics(self, section: str) -> Optional[Dict[str, float]]:
        if not config.has_section(section):
            return None
        gathered_metrics: Dict[str, float] = {}
        for key in config.options(section, True):
            value = self.get_metric_value(config[section][key])
            if value is not None:
                gathered_metrics[key] = value
        return gathered_metrics
