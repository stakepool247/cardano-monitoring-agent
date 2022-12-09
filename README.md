# StakePool247 Cardano Stake Pool Monitoring scripts

The scripts are used to monitor your stake pool and generate leadership schedule as well as monitor the block production of your stake pool.

Currently we have 2 scripts:

### cardano-monitoring-agent

This is a simple monitoring agent for your stake pool. The script is sending the data every 5 minutes to the StakePool247 API and our monitoring system is alerting you if something is wrong with your stake pool.

The script is sending the data every 5 minutes. The script is sending the following data:

- disk usage
- memory usage
- cpu usage
- KES period (under construction)

We are planning to implement also external checks like:

- checking if your metadata file is available online
- check if pledge is met
- check if stake pool has the correct opcert.
- and more...

### leadership-generator

leadership-updater script is generating the leadership schedule for your stake pool.

This script is generating cardano pool's leadership schedule

### Quick Setup guide

1. Register free account at https://app.stakepool247.io
2. Claim your Stake Pool at https://dev.stakepool247.io/devices/add
3. check/copy your access token at https://dev.stakepool247.io/profile  
   this token will be used in your scripts
4. download the bash script:

```
curl -o block_updater.sh https://raw.githubusercontent.com/stakepool247/cardano-monitoring-agent/main/leadership-generator/block_updater.sh
```

add executable mode bit:

```
chmod +x block_updater.sh
```

5. edit the configuration file:
   a) directly in the block_updater.sh OR create leadership.conf file and place it in the scripts or $HOME folder.\*

_sample confgituration file:_

```
SHELLEY_GENESIS_FILE_PATH="/home/cardano/config/mainnet-shelley-genesis.json"
POOL_ID_FILE="/home/cardano/cnode/keys/pool.id"
VRF_SIGNING_KEY_FILE_PATH="/home/cardano/cnode/keys/pool.vrf.skey"
CARDANO_CLI="/home/cardano/.local/bin/cardano-cli"
SOCKET="/home/cardano/cnode/sockets/node.socket"
STAKEPOOL247_API_DEVICE_TOKEN=""
```
