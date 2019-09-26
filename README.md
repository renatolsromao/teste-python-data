# Teste Desenvolvedor Python e Data

O objetivo desse teste é buscar todos os livros sobre o Tema "Python" 
na API do [Open Library](https://openlibrary.org) e salvar a resposta 
em um arquivo JSON para processamento posterior.

Para fazer isso é recomendado utilizar o método 
[Search](https://openlibrary.org/dev/docs/api/search), especificando o
parametro "subject" como "python".

## Exemplo 

```
GET http://openlibrary.org/search.json?subject=python 
```

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