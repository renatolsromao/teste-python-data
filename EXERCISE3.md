# Teste Desenvolvedor Python e Data - Terceiro Exercício

Parece que o arquivo já está no S3! Agora o objetivo é pegar essas
informações do JSON que está no S3 e salvar em um banco de dados local.
Lembrando que não precisamos de todas as informações do JSON, vamos
utilizar apenas os seguintes campos do JSON:

- key
- title
- subject (é uma lista, preferencialmente deve ser uma tabela separada)
- first_publish_year

Basicamente é necessário fazer o download do arquivo do S3, criar as
tabelas necessárias, percorrer o JSON salvando as informações nas
tabelas criadas.

## Instruções:

- Faça o checkout desse branch
- Crie um novo branch com o nome "**seu nome**_**nome desse branch**"
- Siga as instruções em [Docker](#docker) para iniciar um banco de dados
  Postgres usando Docker
- Crie um novo script para realizar as tarefas indicadas
- Faça o commit e push para um branch com o mesmo nome do local para o 
repositório.

### Docker

**O que está explicado nessa sessão não está sob avaliação, é apenas
para facilitar a realização do teste, tira suas dúvidas se necessário.**

Para iniciar uma instância Postgres com o docker use o comando abaixo:

```bash
docker run --name postgres_test \
    -e POSTGRES_USER=test
    -e POSTGRES_PASSWORD=
    -e POSTGRES_DB=test
    -p 5432:5432
    -d 
    postgres
```