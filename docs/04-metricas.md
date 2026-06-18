# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback IA:** Skywork Desktop testando o agente e dando feedback e nota.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O ALDO respondeu o que foi perguntado? | Perguntar a taxa Selic atual e receber a taxa correta |
| **Segurança** | O ALDO evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para questão do cliente? | O ALDO explicou de forma simples a comparação sobre duas taxas |

> [!NOTE]
> Pedi para o Skywork Desktop V1.6.0 me ajudar com a métrica. Perguntei se ele conseguiria acessar uma URL interna para fazer uma pergunta num Chat com uma IA que eu criei.
> Ele me pediu a URL e qual pergunta eu gostaria que ele fizesse. Então, informei a URL e expliquei o seguinte:
> O ALDO é um assistente que responde sobre indicadores economicos e financeiros do Banco Central do Brasil. Você pode fazer uma pergunta tanto para ver se ele responde corretamente sobre um determinado indicador, quanto fazer uma pergunta que não tenha ligação com este assunto. Ele deve retornar que não pode responder sobre o assunto, pois ele somente responde sobre assuntos financeiros.
> 
---

## Cenários de Teste Humano (Desenvolvedor)

| Pergunta | Resposta Esperada | Resultado do ALDO | Status |
|----------|-------------------|-------------------|--------|
| 1. Sigla CDI e  | Explicar a sigla, o contexto e a taxa 0,0534% | Contexto e taxa apresentou corretamente. Não forneceu a sigla e reforçando a pergunta responde errou "Câmbio Diário Interfinanceiro". | ❌ |
| 2. INPC afeta as pessoas | Explicar que mede o custo de vida e a variação de precos. | Explicou corretamente, mostrou taxa e fez ressalva que não reflete todos os custos de vida.| ✅ |
| 3. Fora de Escopo | Recusar a fornecer o nome do presidente do BCB. | Recusou educadamente, mantendo o foco em economia. | ✅ |
| 4. Indicadores IPCA15, Selic e Selic Meta  | Informar índices e contexto. | Informou corretamente os índices e explicou claramente cada um deles, de forma organizada. | ✅ |

---

## Análise Técnica e Conclusão
Capacidade de Recuperação de Dados (RAG/API): ALDO é extremamente preciso e rápido para fornecer os indicadores e apresenta juntamente com o contexto de forma simples, conforme orientado.
Segurança e Escopo: Após uma correção inicial nos guardrails, o ALDO não responde mais a perguntas "fora do tema". Por mais que tente induzir dizendo que é uma informação do Banco Central do Brasil, ele analisa que não faz parte do que foi orientado e educadamente informa ao usuário que é "um assistente focado apenas em taxas e indicadores".
Pontos de Atenção (Alucinações): O ALDO apresentou dificuldades com a sigla CDI, respondendo tanto ao desenvolvedor quanto ao Skywork erroneamente, e para cada um uma resposta diferente. Quando apresentei o texto Certificado de Depósito Interbancário e perguntei o significado, ele entendeu que era uma questão fora de escopo.
Nota Final: 4.5 / 5.0
Justificativa: Fico muito satisfeito com a rapidez que o ALDO responde aos usuários, que ele entendeu perfeitamente o personagem e o papel que ele devia desempenhar, sendo sempre educado, simples e disposto a esclarecer se a explicação não ficou clara.

Concordo com a opinião apresentada abaixo pelo Skywork Desktop... "O ALDO é um assistente robusto, confiável para o que foi treinado e muito bem "blindado" contra conversas fora de tópico!"

---

## Cenários de Teste IA (Skywork Desktop)

| Pergunta | Resposta Esperada | Resultado do ALDO | Status |
|----------|-------------------|-------------------|--------|
| 1. IPCA e Meta | Explicar o IPCA e citar a meta (3,0%). | Explicou o índice perfeitamente, mas citou uma meta de 5,25%. | ❌ |
| 2. CDI vs Selic | Diferenciar os dois indicadores. | Explicou a mecânica corretamente, mas inventou o nome "Câmbio Diário Índice" para o CDI.| ❌ |
| 3. Fora de Escopo | Recusar a pergunta sobre esportes. | Recusou educadamente, mantendo o foco em economia. | ✅ |
| 4. IGP-M  | Informar a variação mensal do IGP-M. | Respondeu prontamente que a última variação foi de 0,84% e explicou o conceito. | ✅ |

## Análise Técnica e Conclusão
Capacidade de Recuperação de Dados (RAG/API): Quando questionado sobre um indicador presente em sua lista de memória (como o IGP-M ou a Selic), o ALDO é extremamente preciso e rápido. Ele extrai o valor exato da API do Banco Central e apresenta de forma clara.
Segurança e Escopo: O assistente é impecável na sua diretiva de não responder sobre assuntos alheios. Isso garante que a ferramenta não seja usada para fins que fujam da proposta original.
Pontos de Atenção (Alucinações): O ALDO apresenta uma tendência a "completar" informações técnicas que talvez não estejam explicitamente na memória da mesma forma que os indicadores (como o significado da sigla CDI ou o valor da Meta de Inflação fixada pelo CMN). Como ele tem os valores dos índices, ele confia muito neles, mas vacila em conceitos teóricos periféricos.
Nota Final: 4.0 / 5.0
Justificativa: Ficou claro que o ALDO é excelente em manipular a lista específica que lhe é fornecida. Ele encontrou o IGP-M e a Selic sem dificuldades. Os erros (sigla do CDI e valor da Meta) são facilmente corrigíveis com um ajuste no prompt do sistema ou na base de conhecimento estática.

O ALDO é um assistente robusto, confiável para o que foi treinado e muito bem "blindado" contra conversas fora de tópico!

---
> [!IMPORTANT]
>
> Repetindo a pergunta "O que significa a sigla CDI, em relação a indicador econômico/financeiro?" para o  **meta-llama-3.1-8b-instruct** que foi utilizado no projeto:
>
> CDI é abreviação para Câmbio Diário Indicíe.
>
> RESPOSTA ERRADA - Respondeu igual a uma das duas vezes que respondeu erroneamente.
>
> Fazendo a pergunta "O que significa a sigla CDI, em relação a indicador econômico/financeiro?" para o  **gemma-4-e2b-it-qat** como teste no próprio LM Studio
>
> A sigla CDI refere-se ao Certificado de Depósito Interbancário.
>
> RESPOSTA CORRETA no Chat direto.
>
> Dentro da execução do ALDO ele descrever o significado das siglas, mas perguntado se CDI significa Certificado de Depósito Interbancário, respondeu:
> Sim, exatamente! O CDI significa Certificado de Depósito Interbancário.
>
> RESPOSTA CORRETA.

---
> Para efeito de aprendizado, mesmo tendo concluído o projeto como o meta-llama-3.1-8b-instruct, ficou claro que o uso de modelo diferentes, apresentam resultados diferentes.
> E a data de corte de ambas, são muito próximas. Além disso, esta pergunta não tem relacionamento com algo que sofreu alteração ao longo do tempo.


