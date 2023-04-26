# DevWeb-Desafio2

## Objetivo: 
<p> Implementar ao projeto <a href="https://github.com/pedroansdev/DevWeb-Desafio2/">DevWeb-Desafio2</a> uma base de dados <a href="https://www.w3schools.com/sql/">SQL</a> </p>

### Tecnologias utilizadas:
<ul>
  <li> Tecnologias do Desafio 2 </li>
  <li> SQL </li>
</ul>

##

### Códigos e Tags utilizadas:

<ul>
  <li> <b>HTML5</b>
    <ul>
      <li>Todas as tecnologias do Desafio 2</li>
      <li>Envio de dados ao app.py através do método POST</li>
    </ul>
  </li>
  <li> <b>CSS3</b>
    <ul>
      <li>Todas as tecnologias do Desafio 2</li>
    </ul>
    <li> <b>Python</b>
    <ul>
      <li>Biblioteca MySql para conexão com Banco de Dados</li>
    </ul>
    <li> <b>Flask</b>
    <ul>
      <li>Todas as tecnologias do Desafio 2</li>
    </ul>
    <li> <b>SQL<b>
    <ul>
      <li>Create & Use Database</li>
      <li>Create & Select from Table</li>
      <li>Insert into Table</li>
    </ul>
</ul>

<span id="etapaExe">

## Como Executar

1. Baixe o repositório em alguma pasta local
2. Na url da pasta principal(DevWeb-Desafio3), digite "cmd" e dê enter

<details>
  <summary>Bem aqui ó 👇</summary>
  <img src="https://cdn.discordapp.com/attachments/733064358694748303/1100916728558534827/image.png">
</details>

3. Insira os seguintes códigos:

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```
_Obs.: Caso você não consiga executar o pip, instale o python 3.11.2, e na hora da instalação, não se esqueça de selecionar a opção de instalação do pip junto_

4. Após todos todos estes passos, abra o link http://127.0.0.1:5000 para finalmente aproveitar o site
5. Depois que você terminar de utilizar o site, não esqueça de executar o seguinte comando(no cmd) para sair do ambiente virtual:
```
deactivate
```

## Observação Essencial

Para rodar o projeto, primeiro você terá que se certificar de que possui o serviço do MySQL em seu computador, caso não tenha ainda, recomendo que baixe uma versão recente do MySQL para tê-lo, logo após isso você seguirá os seguintes passos:

1. Vá na barra de pesquisa de seu computador (não do navegador, e sim do próprio Windows) e pesquise por ```Serviços```, então ache o serviço ```MySQL``` e clique para iniciá-lo.

2. Logo após a primeira etapa, você abrirá o SBGD(Sistema Gerenciador de Banco de Dados) de sua preferência, e lá você colocará o arquivo ```unes.sql```, que pode ser encontrado na pasta <a href="https://github.com/pedroansdev/DevWeb-Desafio3/tree/main/database"> database </a>

3. Após criar certinho o banco de dados e executá-lo em seu computador, vá ao arquivo ```app.py``` e mude as configurações de acesso ao BD, já que cada usuário pode colocar acessos diferentes, estas modificações você fará nas linhas 6 - 8 do arquivo, com suas configurações

4. E é isso, depois disso você poderá seguir os passos da Etapa <a href="#etapaExe"> "Como executar" </a> deste mesmo repositório
