# lns
Repositorio para Atividade da disciplina de Meta Heurística de solucionar o PTHU proposto pelo ITC2007 utilizando a meta heuristica Large Neighborhood Search

## organizacao

O repositório esta organizado conforme os seguintes folders:

1. [[docs](docs)] contendo toda documentação do projeto, com as instruções, referencias, e o artigo produzido 
2. [[src](src)] contem o codigo desenvolvido
3. [[tests](tests)] contem as instancias para teste e avaliação do projeto
4. [[results](results)] contem os resultados obtidos a partir das instancias
5. [[tools](tools)] contem ferramentas complementares para o codigo, inclui o benchmark de tempo de instancia

## descrição do problema

[diagrama](https://online.visual-paradigm.com/app/diagrams/#diagram:workspace=ljaflphy&proj=0&id=2&type=ClassDiagram&width=11&height=8.5&unit=inch?themeSketch=1)

A partir dos dados da instancia devemos criar uma solução que possibilite alocar as disciplinas em que se respeite as 4 restrições hards e minimize as 4 restrições softs:

#### Restrições Fortes:

1. **Aulas**: Todas as aulas de uma disciplina devem ser alocadas, e em períodos diferentes. Uma violação ocorre se uma aula não é alocada, ou se duas aulas da mesma disciplina são alocadas no mesmo período.

2. **Ocupação de Sala**: Duas aulas não podem ser alocadas em uma mesma sala e no mesmo período. Cada aula extra em uma mesma sala e no mesmo período conta como uma violação.

3. **Conflitos**: Aulas de disciplinas de um mesmo currículo, ou ministradas pelo mesmo professor devem ser alocadas em períodos diferentes. Duas aulas conflitantes no mesmo período representa uma violação.

4. **Indisponibilidade**: Se o professor de uma disciplina não está disponível para lecioná-la em determinado período, nenhuma aula dessa disciplina pode ser alocada nesse período. Cada aula alocada em um período não disponível para a disciplina conta como uma violação.

#### Restrições Fracas:
1. **Capacidade de Sala**: Para cada disciplina, o número de alunos que está matriculado na disciplina deve ser menor ou igual ao número de assentos disponíveis em todas as salas que ocorrem aulas dessa disciplina. Cada aluno acima da capacidade conta como uma violação.

2. **Número Mínimo de Dias de Aula**: As aulas de uma disciplina devem ser espalhadas em um número mínimo de dias. Cada dia abaixo do número mínimo de dias conta como uma violação.

3. **Aulas Isoladas**: Aulas de disciplinas de um mesmo currículo devem ser adjacentes uma à outra. Para cada currículo, uma violação é contada quando há uma aula não adjacente à nenhuma outra aula do mesmo currículo no mesmo dia.

4. **Estabilidade de Sala**: Todas as aulas de uma disciplina devem acontecer na mesma sala. Cada sala distinta usada para aulas dessa disciplina, além da primeira, contam como uma violação.

## solucao - lns


***adicionar pseudocodigo do LNS***


Para solucionar o problema, temos como proposta preencher uma matriz de 3 dimensões em que 
![estrutura de solucao](https://4.bp.blogspot.com/_AojK1cTeQfU/S0eSeQzFZ0I/AAAAAAAAAJM/SvhcMnw8Gzs/s320/matriz_3d.JPG)
