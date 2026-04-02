# Exercício Prático: Orquestração de API Python com Banco de Dados

**Objetivo:** Criar um arquivo `docker-compose.yml` que orquestre três serviços interligados, permitindo o desenvolvimento local com *live-reload* na aplicação Python e garantindo a persistência do banco de dados.

## Requisitos 

Crie o arquivo docker-compose.yml na raiz do diretório do projeto que atenda estritamente aos seguintes requisitos:

**Serviço 1: Banco de Dados (`db`)**
* Imagem: `postgres:15-alpine`
* Variáveis de ambiente para criar o banco: `POSTGRES_USER=app_user`, `POSTGRES_PASSWORD=app_pass`, `POSTGRES_DB=app_db`.
* Volume nomeado chamado `pg_dados` mapeado para `/var/lib/postgresql/data`.

**Serviço 2: Interface de Administração (`admin`)**
* Imagem: `dpage/pgadmin4`
* Variáveis de login: `PGADMIN_DEFAULT_EMAIL=admin@admin.com` e `PGADMIN_DEFAULT_PASSWORD=admin`.
* Porta exposta: `8080` (host) mapeada para `80` (contêiner).
* Dependência: Deve aguardar o serviço `db` iniciar.

**Serviço 3: Aplicação API (`api`)**
* Construção local (`build`) utilizando o `Dockerfile` do diretório atual.
* Porta exposta: `5000` mapeada para `5000`.
* **Bind Mount:** Mapear o diretório atual (`.`) para o diretório `/app` dentro do contêiner, permitindo que alterações no `app.py` reiniciem o servidor Flask automaticamente.
* Dependência: Deve aguardar o serviço `db` iniciar.


## Roteiro de Validação

1. Subir a infraestrutura (`docker compose up -d`).
2. Acessar `http://localhost:5000/init` para criar a tabela.
3. Acessar `http://localhost:5000/registrar` algumas vezes e verificar o contador subindo.
4. Alterar a mensagem de retorno na rota principal (`/`) do arquivo `app.py` no host, salvar, atualizar a página `http://localhost:5000` e provar que o *live-reload* do bind mount está funcionando.
5. Acessar o pgAdmin (`http://localhost:8080`), conectar ao banco usando o host `db` e verificar se os dados estão na tabela `logs`.
