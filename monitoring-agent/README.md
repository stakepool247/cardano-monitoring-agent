# Stakepool247 agent

Python agent that collects statistics from prometheus and sends them to stakepool247 metrics API.

## Requirements

Install requirements using command:

```
pip3 install -r requirements.txt
```

## Usage

Copy `config.ini.sample` to `config.ini` file and add generated `device_key` to the config.
If necessary, change additional configurations.

Run the agent by running

```
python3 stakepool247-agent/main.py --config-file config.ini
```

To run the agent continuously, configure the following cronjob, replacing `{AGENT_PATH}` with actual path of the agent directory:

```
*/5 * * * * /usr/bin/python3 {AGENT_PATH}/stakepool247-agent/main.py --config-file {AGENT_PATH}/config.ini
```