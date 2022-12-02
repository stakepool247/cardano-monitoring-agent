import argparse

parser = argparse.ArgumentParser(description='Stakepool247 Agent', prog="stakepool247-agent")
parser.add_argument('--config-file', type=str, help='Path to configuration file')

args = parser.parse_args()