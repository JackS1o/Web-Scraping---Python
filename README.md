## Raspagem de dados com Python

Para rodar a aplicação localmente, basta executar os comandos:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install

```

## Após a instalação das dependências, basta executar o comando:

```bash
python crawler.py

```
## Acesse a API em:

```bash
http://localhost:5000/

```

Esta aplicação foi desenvolvida com as seguintes tecnologias:

Python, com a biblioteca Playwright para automatizar o navegador e extrair os dados e a biblioteca Flask para criar e deixar os dados disponíveis em uma API.


O objetivo era consumir uma URL, filtrar os dados e retornar uma lista de objetos com apenas laptops da marca Lenovo.