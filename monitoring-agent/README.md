# Stakepool247 agent

Python agent that collects statistics from prometheus and sends them to stakepool247 metrics API.

## Usage

Copy `config.ini.sample` to `config.ini` file and add generated `device_key` to the config.
If necessary, change additional configurations.

Start the agent by running

```
python3 -m stakepool247-agent --config-file config.ini
```
