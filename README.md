# LFA - Moore | Mealy

**Autores:** Emanuel Rampinelli Gloria e Rafael dos Anjos;

**Introdução**
Implementação dos algoritmos de conversão de autômatos ﬁnitos com saída .
  - Conversão de Máquina de Mealy para Máquina de Moore equivalente.
  - Conversão de Máquina de Moore para Máquina de Mealy equivalente.

**Sintaxe dos Arquivos de Entrada**;

A primeira linha do arquivo de entrada terá apenas uma palavra, “mealy” ou “moore”, indicando o tipo de máquina que o arquivo descreve;

**Mealy**

 - **Linha 1**: conterá a palavra mealy;  
 
 - **Linha 2**: conterá uma sequência de strings separadas por espaços representando os nomes dos estados. Por exemplo: s0 s1 s2 s3 s4 sf. 
 
 - **Linha 3**: conterá uma sequência de símbolos separados por espaços representando o alfabeto de entrada.1 Por exemplo: a b c.
 
 - **Linha 4**: conterá o nome do estado inicial.
 
 - **Linha 5**: conterá uma lista com o nome dos estados ﬁnais, separados por espaçoos. Caso não haja estados ﬁnais, esta linha estará a string --.
 
 - **Linha 6**: conterá uma sequência de símbolos separados por espaços representando o alfabeto de saída. Por exemplo: X Y Z. 
 
 - **Linha 7 em diante**: representam a função de transição, e cada linha terá o seguinte formato: 
 
 1. nome do estado inicial 
 2. símbolo da transição (da cadeia de entrada)
 3. nome do estado ﬁnal
 4. lista de símbolos de saída (zero ou mais símbolos de saída)

**Moore**

- **Linha 1**: conterá a palavra moore;

- **Linha 2**: conterá uma sequência de strings separadas por espaços representando os nomes dos estados. Por exemplo: s0 s1 s2 s3 s4 sf.

- **Linha 3**: conterá uma sequência de símbolos separados por espaços representando o alfabeto de entrada. Por exemplo: a b c.

- **Linha 4**: conterá o nome do estado inicial.

- **Linha 5:** conterá uma lista com o nome dos estados ﬁnais, separados por espaços. Caso não haja estados ﬁnais, esta linha conterá a string “--” (sem as aspas).

- **Linha 6**: conterá uma sequência de símbolos separados por espaços representando o alfabeto de saída. Por exemplo: X Y Z.

- **Linhas 7...(7+n)**: representam a função de transição, e cada linha terá o seguinte formato: 
1. nome do estado inicial 
2. símbolo da transição (da cadeia de entrada) 
3. nome do estado ﬁnal •

- **Linha (7 + n) + 1**: contém a string “-----” (sem as aspas). Esta linha funciona como um marcador para o ﬁnal da deﬁni¸ca˜o da função de transic¸˜ao do autˆomato.

- **Linha (7 + n) + 2 em diante**: contém a deﬁnição da saída da Máquina de Moore. Deve haver uma linha para cada estado deﬁnido na linha 2 do arquivo. Cada linha terá o nome do estado no início, seguido por uma sequência de zero ou mais símbolos do alfabeto de saída, separados por espaço.

**Comando de execução** :
 python3 <arquivo. py> <entrada.txt> <saida.txt>;
 
 






