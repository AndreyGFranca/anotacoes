# Introdução

O diagrama de classe é um dos mais importantes e mais utilizados da UML. Seu principal objetivo é vizualizar as classes que comporão o sistema, bem como demostrar como elas se relacionam entre si. Basicamente o diagrama de classe é composto por suas classes e pelas associações (relações) existente entre elas.

Embora os métodos e os atibutos são todos colocados no diagrama de classe, o mesmo não trata o que cada um irá realizar, o que é trabalho de outro diagrama, o diagrama de atividade.

Uma classe é representada por um retangulo contendo três divisões:
A primeira divisão contém o nome da classe. A segunda armazena os atributos da classe. A terceira os métodos.

**Exemplo:**   
![](imgs/img006.png)

# Relacionamentos ou Associações
As classes constumam ter relacionamentos, entre si, chamados associações, que permitem que elas compartilhem informações entre sí e colaborem para a execução dos processos executados pelo sistema.

## Associação Unária ou reflexiva
Essa associação acontece quando um objeto da classe tem relação com objetos da mesma.

![](imgs/img007.png)

Neste exeplo temos uma linha saindo da classe Funcionario e chegando na própria classe, isto é porque um funcionario pode chefiar um funcionario, como pode ser visto no texto ao lado da linha, também podemos ver 0 .. \* isto é a **multiplicidade**. A multiplicidade procura determinar o numero minimo e maximo de objetos envolvidos em cada extremidade da associação, além de permitir especificar o nível de dependência de um objeto para com os outros envolvidos na associação. No caso apresentado, significa que 1 funcionarios pode chefiar 0 ou muitos (\*) funcionarios. Quando **não existe multiplicidade explícita** entende-se que a multiplicidade é "1..1"

## Associação Binária
Associações binárias acontecem quando são identificados relacionamentos entre objetos de duas classes distintas. Esse tipo de associação é, em geral, a mais comunmente encontrada.

![](imgs/img008.png)
