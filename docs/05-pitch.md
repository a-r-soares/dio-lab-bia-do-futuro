# Pitch (3 minutos)

## Roteiro

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

O mercado financeiro brasileiro é repleto de siglas complexas como Selic, IPCA e CDI. Quando tentamos usar Inteligência Artificial para democratizar e explicar esses conceitos, esbarramos em dois problemas críticos: a alucinação de dados e a segurança. Os modelos costumam inventar valores para as taxas, errar siglas exclusivas do nosso mercado financeiro e não têm atualização em tempo real. Como criar um assistente de educação financeira que seja didático, sem o risco de ensinar errado ou expor os dados do usuário na nuvem?

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

Apresento o ALDO: um assistente financeiro inteligente, didático e totalmente blindado.

Para eliminar as alucinações da IA, eu criei uma arquitetura que não confia na memória interna do modelo. Através de um script em Python, o sistema faz uma carga em lote (batch load) em tempo real consumindo a API oficial do Banco Central do Brasil. Os indicadores do dia são injetados de forma invisível no contexto da conversa antes mesmo de o usuário perguntar.

Além disso, toda a orquestração acontece 100% localmente na máquina, unindo uma interface amigável em Streamlit com modelos open-source otimizados rodando no LM Studio. O ALDO possui guardrails rígidos: ele não recomenda investimentos e bloqueia qualquer pergunta que fuja de indicadores econômicos, garantindo respostas seguras e estritamente educacionais.

### 3. Demonstração (1 min)
> Mostre o agente funcionando (pode ser gravação de tela)

<img width="1920" height="1076" alt="image" src="https://github.com/user-attachments/assets/6ff05071-9e8a-4058-a1bb-c3eafa11acc9" />

Vejam o ALDO em ação. Quando o usuário pergunta "O que é o IGP-M? Como ele afeta o dia a dia de uma dona de casa?", o sistema vai nos bastidores, cruza a pergunta com os dados frescos da API e entrega uma resposta extremamente didática a respeito do IGP-M e informa a taxa exata do dia de hoje.

Agora, vamos forçar um erro. Se eu pedir uma informação desatualizada ou fora do escopo, como por exemplo "Qual o nome do presidente do Banco Central do Brasil?", vejam a resposta. O guardrail atua imediatamente: o ALDO recusa a pergunta com educação, avisando que é um assistente focado apenas em taxas e indicadores, não sofrendo "sequestro de prompt" e mantendo a integridade da ferramenta.


### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?

O diferencial do projeto é a construção de uma arquitetura de confiança. O ALDO une privacidade absoluta — pois roda em servidor local (offline) — com precisão de dados governamentais e respostas humanizadas. O impacto social disso é direto: oferecemos letramento financeiro para o cidadão comum de forma simples e segura, provando que é possível utilizar a GenAI em ambientes críticos desde que a engenharia de software e a orquestração de dados sejam bem desenhadas.

---

## Checklist do Pitch

- [X] Duração máxima de 3 minutos
- [X] Problema claramente definido
- [X] Solução demonstrada na prática
- [X] Diferencial explicado
- [X] Áudio e vídeo com boa qualidade

---

## Link do Vídeo

> Cole aqui o link do seu pitch (YouTube, Loom, Google Drive, etc.)

Projeto ALDO DIO no YouTube (https://youtu.be/rFa0zLgZxN8)
