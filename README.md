# Exemplo de uso:
<p align="center">
<a href="https://www.circuitlab.com/circuit/2fxrr6s3kxd2/exemplo/"><img src="https://www.circuitlab.com/circuit/2fxrr6s3kxd2/screenshot/540x405/"/></a>
</p>


## Executando

`python path/to/phasor_calc.py`


### O programa realizará uma serie de perguntas a respeito do seu circuito:

- Primeiro, o programa perguntará se foi dada a velocidade ângular ou a frequência, com as respostas sendo respectivamente **w** ou **f**:
<p align="center">
<img src=img/step2.png>
</p>

- Agora basta entrar os nomes e valores dos componentes presentes no circuito: (Note que os componentes podem ter qualquer nome, ja que são separados por um dicionário onde os nomes são as "keys" e os valores são os "values")
<p align="center">
<img src=img/step3.png>

- Tendo posto todos os componentes e seus valores, o programa irá devolver a impedância de cada elemento na forma retângular e polar:
<p align="center">
<img src=img/step4.png>
</p>

- Agora o programa pergunta se os componentes estão ou não em serie ou se quer pular este passo, e devolverá a impedância equivalente nas formas retângular e polar: 

*Se existir componentes em paralelo, será necessário alterar a linha 111 do código em uma IDE, colocando a equação que calcule a impedância equivalente do circuito*
<p align="center">
<img src=img/step5.png>
</p>

- Se quiser que o programa calcule a corrente e realize análises sobre a potência do circuito, serão necessários o valor da DDP de pico-a-pico ou a DDP eficaz, assim como o ângulo de fase da onda 

(exemplo:   <img src="https://latex.codecogs.com/gif.latex?4\cdot&space;\cos&space;\left&space;(&space;\omega&space;t&space;&plus;&space;46&space;\right&space;)" title="4\cdot \cos \left ( \omega t + 46 \right )" />    Vpp=4, fase=46º)
<p align="center">
<img src=img/step6.png>
</p>

- Finalmente, devolvendo os valores análizados!
<p align="center">
<img src=img/step7.png>
</p>
