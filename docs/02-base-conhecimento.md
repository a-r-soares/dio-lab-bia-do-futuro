# Base de Conhecimento

## Dados Utilizados

- Fonte Principal de Dados:

  Acesso transacional dinâmico à API pública do Banco Central do Brasil (SGS - Sistema Gerenciador de Séries Temporais).

- Armazenamento Local (Persistência de Dados):

  Nenhum. O projeto adota a arquitetura de processamento em memória (in-memory), dispensando a criação de diretórios locais de dados (ex: pastas de arquivos .csv ou .json).

- Justificativa de Arquitetura:

  - Acurácia (Real-Time):

    Garante que o assistente (ALDO) utilize estritamente a informação oficial do exato momento da consulta, mitigando o risco de respostas com base em arquivos locais desatualizados.

  - Otimização de Recursos:

    Elimina a necessidade de desenvolver rotinas paralelas de carga e atualização de dados (ETL físico), mantendo o sistema incrivelmente leve e eliminando pontos de falha de armazenamento.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não há modificação dos dados lidos pela API.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O carregamento ocorre de forma dinâmica e transacional (sob demanda). No momento da interação com o assistente, o back-end em Python realiza uma requisição HTTP (método GET) diretamente aos endpoints da API do Sistema Gerenciador de Séries Temporais (SGS) do Banco Central. O retorno (payload), em formato estruturado JSON, é imediatamente processado pela aplicação. Os campos essenciais — como a data de vigência e o valor percentual da taxa — são extraídos e carregados estritamente na memória volátil (RAM) através de variáveis do código. Não há rotinas de persistência física (gravação em disco), garantindo que o sistema consuma sempre a posição mais atualizada e oficial sem gerar lixo de dados.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados extraídos da API atuam como o contexto de ancoragem para o modelo de linguagem (Gemma 4). As variáveis que estão em memória são injetadas dinamicamente no System Prompt (as instruções de base do assistente) utilizando técnicas nativas de formatação de texto do Python (como as f-strings).
Na prática, o código acopla a regra de negócios à informação oficial antes de chamar o servidor do LM Studio, enviando uma instrução semelhante a: "Você é o ALDO. O usuário tem uma dúvida. Baseie sua explicação exclusivamente neste dado oficial: A taxa Selic referente a [variável_data] é de [variável_taxa]%." Essa injeção de contexto trava o LLM na verdade absoluta do dado, eliminando o risco de alucinações e garantindo que o motor de inferência foque apenas em traduzir o número para uma linguagem didática e acessível ao usuário final.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
 "Você é o ALDO. O usuário tem uma dúvida. Baseie sua explicação exclusivamente neste dado oficial:
  A taxa Selic referente a [variável_data] é de [variável_taxa]%."
...
```
