# StakePool247 Cardano Stake Pool Monitoring scripts (draft)

## leadership-generator

This script is generating cardano pool's leadership schedule

###  Quick Setup guide
1. Register free account at https://app.stakepool247.io 
2. Claim your Stake Pool at https://dev.stakepool247.io/devices/add
3. check/copy your access token at https://dev.stakepool247.io/profile  
	this token will be used in your scripts
4. download the bash script:
`curl -o block_updater.sh https://raw.githubusercontent.com/stakepool247/cardano-monitoring-agent/main/leadership-generator/block_updater.sh`

add executable mode bit 
`chmod +x block_updater.sh`

5. edit the configuration file:
a) directly in the block_updater.sh  OR create leadership.conf file and place it in  the scripts or $HOME folder.\

_sample confgituration file_

SHELLEY\_GENESIS\_FILE\_PATH="/home/cardano/config/mainnet-shelley-genesis.json"
POOL\_ID\_FILE="/home/cardano/cnode/keys/pool.id"\
VRF\_SIGNING\_KEY\_FILE\_PATH="/home/cardano/cnode/keys/pool.vrf.skey"\
CARDANO\_CLI="/home/cardano/.local/bin/cardano-cli"\
SOCKET="/home/cardano/cnode/sockets/node.socket"\
STAKEPOOL247\_API\_DEVICE\_TOKEN=""

6. execute the script manually or add it to the crontab
7. on success check the results at https://app.stakepool247.io - you should see the new added blocks in the graphs.


our monitoring system will check if these blocks will be successfully minted.
