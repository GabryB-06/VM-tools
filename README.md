
# VM tools

Script Python per inviare files da una VM (dovrebbe andare bene anche per trasferire da qualsiasi dispositivo connesso in LAN) verso la macchina che sta eseguendo questo backend

## Utilizzo (guest -> host)

Eseguire lo script e collegarsi in HTTP verso l'IP della macchina che sta eseguendo il backend sulla porta 5000 (es. `http://192.168.1.25:5000`)

## Tool simili (host -> guest)

Per passare file dall'host verso la VM si può eseguire `python3 -m http.server` e collegarsi dalla VM verso l'IP della macchina che sta eseguendo il server in HTTP sulla porta 8000 (es. `http://192.168.1.25:8000`)

## Software di virtualizzazione testati

- Oracle VM Virtualbox

- VMware Player
