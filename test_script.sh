# script for running in github codespaces

workspaces=true

if $workspaces
then
    /home/codespace/.python/current/bin/python3 /workspaces/lns/src/main.py </workspaces/lns/instances/toy
else
    python3 src/main.py <instances/toy
fi