# Código da Aplicação

Esta pasta contém o código do agente ALDO.

## Estrutura

```
src/
   ├── aldo_app.py         # Aplicação Utilitária (Terminal / CLI) - Script Python puro focado em automação, processamento em lote e execução rápida direto no terminal.
   ├── aldo_web.py         # Aplicação Principal (Web / Streamlit) - Interface gráfica interativa para o usuário (chat).
   |── requirements.txt    # Dependências
   └── .dotenv             # Dados Sensíveis -  URL e KEY para o aplicativo aldo_app.py
.strealit/
   └── secrets.toml        # Dados Sensíveis -  URL e KEY para o aplicativo aldo_web.py
```

## Arquivo requirements.txt

```
openai==2.42.0
python-dotenv==1.2.2
requests==2.34.2
streamlit==1.58.0
```
## Antes de Rodar

```
EDIT o arquivo .dotenv e preencha as variáveis de acordo com seu caso
LM_STUDIO_URL = "INFORMAR_AQUI_URL"
LM_STUDIO_KEY = "INFORMAR_AQUI_KEY"

EDIT o arquivo secrets.toml dentro da pasta .streamlit e preencha as variáveis de acordo com seu caso
BASE_URL = "INFORMAR_AQUI_URL"
API_KEY = "INFORMAR_AQUI_KEY"
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação utilitária
python aldo_app.py

# Rodar a aplicação principal
streamlit run aldo_web.py
```

## Evidência de Execução do LM Studio e o Servidor

<img width="1914" height="1028" alt="image" src="https://github.com/user-attachments/assets/eed581bd-841e-45eb-972c-8a05731f5b49" />

---

## Evidência de Execução do Streamlit e o ALDO

<img width="1916" height="938" alt="image" src="https://github.com/user-attachments/assets/4b301a97-2bc1-4724-a826-fa535c69a190" />

---
