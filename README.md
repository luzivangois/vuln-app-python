# API vulnerável em Python

Este projeto foi criado com vulnerabilidades para uso em laboratório como back-end python e rodar localmente

## Requisitos
* VSCode ou outra IDE que rode python
* Python 3.12
* Dependencias listadas em requirements.txt (passo 3 do processo de instalação abaixo)
* Postman ou Insomnia (ou ferramenta similar) - Para interagir com a API

## Instalação

1. Clone o repositório

```bash
git clone https://github.com/luzivangois/vuln-app-python.git
```

2. Crie e Ative o ambiente virtual (.venv) para poder instalar as dependências
   
> Ambiente Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Ambiente Windows (cmd)
```bash
python3 -m venv .venv
.venv\Scripts\activate.bat
```

> Ambiente Windows (powershell)
```bash
python3 -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instale as dependencias com pip3

```bash
pip3 install -r requirements.txt
```

4. Rode a aplicação localmente

> por padrão a aplicação vai rodar na porta 5000 do local host (http://localhost:5000)
```bash
python3 main.py
```

5. Endpoints da API

Os endpoints disponibilizados pela API podem ser acessados utilizando-se a collection existente em /vuln-app-python/tree/main/resources
