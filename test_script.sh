# script for running in github codespaces

runall=false
workspaces=true


exec='/home/codespace/.python/current/bin/python3 /workspaces/lns/src/main.py' # github workspaces
#exec=Python3 src/main.py # ubuntu

#saida='' # saida padrao no terminal
saida='/workspaces/lns/saida/saida.txt'



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


if $runall
then
    for i in ${!instances[@]};do
        echo "Installing ${instances[i]}"
        $exec </workspaces/lns/Instancias/${instances[i]} $saida
    done
else
    #echo "$exec </workspaces/lns/Instancias/toy.ctt $saida"
    $exec </workspaces/lns/Instancias/toy.ctt >$saida
fi
