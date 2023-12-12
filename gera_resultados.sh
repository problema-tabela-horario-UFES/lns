#!/bin/bash
# script for running in github codespaces

runall=true
exec='python3 src/main.py' # ubuntu
saida='results/saida'

tests_folder="tests"
results_folder="results"

timelimit="--timelimit=10"
#saida='' # saida padrao no terminal


instances=(
    "toy.ctt"
    "comp01.ctt"
    "comp02.ctt"
)

all_instances=(
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


echo "Running"

# Run for each instance 5 times
for i in ${!instances[@]};do
    echo "Running instance ${instances[i]}"
    #echo "$exec </tests/${instances[i]} > $saida$i.txt"
    mkdir -p "$results_folder/${instances[i]}"
    #rm $results_folder/${instances[i]}/* -r
    for j in 1 2 3 4 5;do
        #echo "$exec <tests/${instances[i]} > $results_folder/${instances[i]}/solution_${j} $timelimit"
        $exec <$tests_folder/${instances[i]} > $results_folder/${instances[i]}/${j} $timelimit
        #echo "./tools/validator/validator $tests_folder/solution_${instances[i]} $results_folder/${instances[i]}/${j} >$results_folder/${instances[i]}/validator_$j"
        ./tools/validator/validator $tests_folder/${instances[i]} $results_folder/${instances[i]}/${j} >$results_folder/${instances[i]}/validator_$j
    done
done



