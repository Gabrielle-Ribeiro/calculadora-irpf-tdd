### Características - Qualidade de projeto de código

Esse trabalho apresenta 5 características de um bom projeto de software. Trazendo uma descrição sobre cada, uma relação da característica com os maus-cheiros de código e uma operação de refatoração que leva um projeto a ter a característica analisada.

## Ausência de Duplicidades

Segundo Goodliffe (2006), a ausência de duplicidades traz facilidades para a correção de problemas no código, pois proporciona um entendimento melhor do código e ajuda na segurança e manutenção do mesmo. Assim, a duplicação de código é inimiga do design simples e elegante, já que as redundâncias tornam o código mais frágil. Projetos que possuem duplicidades são mais difíceis de manter e menos seguros, pois isso contribui para o surgimento de problemas quando ocorrem modificações em trechos de código que estão duplicados. Assim, um bug pode ser corrigido em um local do código, mas continua existindo em outro local. 

A ausência de duplicidades pode ser associada ao mau-cheiro de código duplicado. Esse mau-cheiro é constituído pela repetição de um mesmo trecho de código em diferentes partes de um projeto. Segundo Fowler (1999), a unificação de um trecho que existe em mais de um ponto do projeto aumenta a qualidade do programa.

Uma operação de refatoração capaz de levar o projeto de código a ter a característica em análise é a de extrair método. Isso pode ser feito quando uma mesma expressão é encontrada em mais de um método da mesma classe. Outra possibilidade é a aplicação de um método template, extraindo os comportamentos comuns desses métodos e implementando a variabilidade em subclasses. 

## Extensibilidade

Segundo Goodliffe(2006), um código bem projetado, apresenta a possibilidade de adição de novas funcionalidades, em locais apropriados. Porém, é fundamental buscar o equilíbrio entre produzir um código extensível mas que não seja completamente focado em lidar com qualquer possível alteração que possa ocorrer. Caso contrário, isto pode criar uma engenharia excessiva ao projeto. Portanto, busca-se estender o código através de plugins, hierarquias de classe e interfaces bem planejadas, funções com retornos úteis e com uma estrutura de código lógica e maleável.

É necessário buscar um equilíbrio ao aplicar a extensibilidade em um projeto. Quando este cuidado é inexistente, encontra-se o mau-cheiro de Generalidade Especulativa. Neste caso, os projetos, visando adicionar novas funções que, em algum momento, poderiam ser implementadas, se tornam genéricos, apresentando maior complexidade para seu entendimento e manutenção.

É possível refatorar o projeto através da diminuição da hierarquia, da incorporação de classe e a remoção de parâmetros. Desta forma, elimina-se o mau-cheiro consequente da especulação da adição de futuras funcionalidades.

## Simplicidade

Uma das características mais importantes quando queremos ter um código bem escrito é a simplicidade, pois ela torna o código mais fácil de aprender, ler e entender, o que afeta a facilidade de escrita. Códigos simples não são necessariamente códigos menores, mas sim códigos que usam estrategicamente o menor número de recursos para que ele seja completamente compreendido.

Quando temos programadores que não estão familiarizados com um código, uma quantidade elevada de construções pode levar a falta ou uso incorreto de recursos que poderiam ser úteis no projeto. 

A simplicidade em um projeto faz com que os seguintes maus-cheiros definidos por Fowler sejam evitados: classes ou métodos longos e duplicação de código.

Uma operação de refatoração possível é a extração de um método. Utilizando a operação de extrair método identificamos um método longo e é possível refatorá-lo visando diminuir seu tamanho, fazendo um código mais simples. 


## Boa documentação

É um documento que explica como o código funciona, desde a sua parte mais básica até a mais complexa. A documentação do software pode auxiliar usuários e programadores sobre as rotinas que estão contidas no software facilitando o uso e o desenvolvimento para futuras evoluções e manutenções. Consiste num conjunto de manuais gerais e técnicos, até 
diagramas explicando o funcionamento do programa como um todo ou cada parte dele.

Em termos gerais, documentações precisam ter três elementos:
detalhes técnicos: familiarizar o responsável por aquela parte do desenvolvimento sobre como, quando e por que aquela intervenção foi realizada.
contextualização de problema: informa cada obstáculo durante o desenvolvimento e em que situação ele ocorreu;
contextualização de solução: explica as modificações feitas em processos ou no código que corrigiram o problema;

Em relação com os maus-cheiros de código definidos por Fowler, uma boa documentação auxilia na manutenção do código, na redução de Códigos Duplicados, Métodos Longos, Classe Grande, Cadeias de Mensagens e Comentários.

Uma boa documentação pode garantir que em uma futura refatoração possa ser tirado comentários desnecessários, já que ele estará devidamente explicado na documentação . Outra melhoria é que a documentação reduz as linhas de código e, consequentemente, a complexidade do código.

## Modularidade

Permite que um projeto de código seja dividido em diversas partes que interagem entre si. Essas partes são denominadas de módulos. O código desenvolvido é dividido em módulos independentes, que podem ser utilizados a qualquer momento, em conjunto ou individualmente. Isso permite que uma parte do código possa ser alterada sem que todo o código já desenvolvido seja modificado. Assim, é muito mais prático atualizar um projeto de código. É preciso lembrar que buscar uma qualidade dentro dessa quebra por módulos do projeto é bastante importante para não se ter problemas de comunicação entre eles.

Uma boa modularidade é preciso ter funcionalidades bem relacionadas entre si e interdependência entre os módulos. Com isso, um módulo pode ser trabalhado e testado isolado sem problemas. Nesse contexto de testes, uma das vantagens da modularidade é a possibilidade de criar testes unitários para os códigos e permitir a divisão de tarefas entre os desenvolvedores.

A Modularidade pode evitar os seguintes maus-cheiros definidos por Martin Fowler: Instruções switch; A obsessão primitiva; Duplicação de código; Generalização especulativa.

É possível refatorar projetos de código extraindo métodos para se alcançar a modularidade. Utilizar a operação "Extrair método" quando a mesma expressão encontra-se em dois métodos ou mais na mesma classe pode ser levado para uma possível refatoração.

