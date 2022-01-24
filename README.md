<h1 align="center">
   Back-end Challenge 🏅 2021 - Space Flight News
</h1>
<p align="center">
   <a>
    <img alt="Python" src="https://img.shields.io/github/languages/top/WalyssonPaiva/spaceflightnews">
  </a>

  <img alt="Repository Size" src="https://img.shields.io/github/repo-size/WalyssonPaiva/spaceflightnews">
	
<a target="_blank" href="https://www.linkedin.com/in/walyssonpaiva">
    <img alt="Made by WalyssonPaiva" src="https://img.shields.io/badge/Made%20By-WalyssonPaiva-brightgreen">
  </a>

  <a>
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/WalyssonPaiva/spaceflightnews">
  </a>

 
  <img alt="Stars total <3" src="https://img.shields.io/github/stars/WalyssonPaiva/spaceflightnews?style=social">
</p>
<h1>
  :clipboard: Projeto:
</h1>
<p>Uma API que possui todos os artigos da Space Flight News API (novos artigos inseridos diariamente às 9h por um cron) e permite a criação, atualização e listagem (CRUD).</p>
<h1>:book:O que eu usei:</h1>
<ul>
<li> Python</li>
<li> FastAPI</li>
<li> MongoDB</li>
<li> Docker</li>
<li> Docker Compose</li>
</ul>

<h2>:information_source: Como usar: </h2>
<p> PS: você precisa ter o Python instalado, preferencialmente na versão 3.8.x </p>
<p> Renomeie o arquivo ".env-sample" para ".env" e preencha as variáveis de ambiente. Ex:</p>

```
DATABASE_CONNECTION=mongodb+srv://<usuario>:<senha>@<url>
COLLECTION=articles
```

Em seu terminal:
```
Clone este repositório:

$ git clone https://github.com/WalyssonPaiva/spaceflightnews
$ cd spaceflightnews

Preenchendo o Banco com os artigos atuais:

$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python lib/seeds.py
```
Executando com Docker Compose (método mais fácil):
```
$ docker-compose up --build
```
Executando com Python:
```
$ python -m uvicorn lib.app:app --reload
```
Executando os testes:
```
$ python -m pytest -vv
```
<h2>Acessando o app:</h2>
<p>http://localhost:8000</p>
<h2>Acessando a documentação</h2>
<p>http://localhost:8000/docs#</p>

> This is a challenge by Coodesh
