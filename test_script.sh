# script for running in github codespaces

runall=false
workspaces=true

instances=(
    "toy.ctt"
    "comp01.ctt"
    "comp02.ctt"
    "comp03.ctt"
    "comp04.ctt"
    "comp05.ctt"
    "comp06.ctt"
    "comp07.ctt"
    "comp08.ctt"
    "comp09.ctt"
    "comp10.ctt"
    "comp11.ctt"
    "comp12.ctt"
    "comp13.ctt"
    "comp14.ctt"
    "comp15.ctt"
    "comp16.ctt"
    "comp17.ctt"
    "comp18.ctt"
    "comp19.ctt"
    "comp20.ctt"
    "comp21.ctt"
)

if $workspaces
then
    
    if $runall
    then
        for i in ${!instances[@]};do
            echo "Installing ${instances[i]}"
            /home/codespace/.python/current/bin/python3 /workspaces/lns/src/main.py </workspaces/lns/Instancias/${instances[i]}
        done
    else
        /home/codespace/.python/current/bin/python3 /workspaces/lns/src/main.py </workspaces/lns/Instancias/toy.ctt
    fi


else
    python3 src/main.py <instancias/toy
fi