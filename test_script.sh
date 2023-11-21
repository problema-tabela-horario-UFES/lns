# script for running in github codespaces

runall=false
exec='python3 src/main.py' # ubuntu
saida='results/saida'
testefile='tests/comp03.ctt'



#saida='' # saida padrao no terminal
saida='results/grafico.txt'


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
        echo "Running instance ${instances[i]}"
        #echo "$exec </tests/${instances[i]} > $saida$i.txt"
        for j in 1 2 3 4 5;do
            $exec <tests/${instances[i]} > ${saida}${i}_${j}.txt
        done
    done
else
    #echo "$exec </workspaces/lns/Instancias/toy.ctt $saida"
    $exec <$testefile > $saida
fi
