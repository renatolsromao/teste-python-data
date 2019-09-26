# Teste Desenvolvedor Python e Data

O objetivo desse teste é buscar todos os livros sobre o Tema "Python" 
na API do [Open Library](https://openlibrary.org) e salvar a resposta 
em um arquivo JSON para processamento posterior.

Para fazer isso é recomendado utilizar o método 
[Search](https://openlibrary.org/dev/docs/api/search), especificando o
parametro "subject" como "python".

Não é necessário tratar a paginação da API, é suficiente apenas uma
requisição!

## Exemplo de chamada para a API

```
GET http://openlibrary.org/search.json?subject=python 
```

## Instruções:

- Faça o checkout desse branch
- Crie um novo branch com o nome "**seu nome**_**nome desse branch**"
- Crie o script para atender o necessário
- Faça o commit e push para um branch com o mesmo nome do local para o 
repositório.


## O que estamos esperando?

Esperamos um script simples, que consiga realizar a tarefa proposta, 
utilizando bibliotecas conhecidas do Python e adequadas para resolver
o problema.

## O que não é necessário?

Não é necessário utilizar conceitos de orientação a objetos e mostrar
entendimento de estruturas mais avançadas da linguagem, esse teste tem
como objetivo ser um teste rápido e testar a habilidade de execução, e 
consideramos que para uma tarefa tão simples não é necessário otimizar 
tanto o código.

## Referência

- [Open Library API](https://openlibrary.org/developers/api)