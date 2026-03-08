# F1 YouTube Analytics - Highlights 2024

Este projeto coleta dados dos vídeos de **highlights das corridas de Fórmula 1 do ano de 2024** no canal oficial do YouTube e envia para o **Google Sheets**, permitindo criar dashboards no **Looker Studio** para análise de audiência e engajamento.

---

## 🎯 Objetivo

- Consumir a API do YouTube e coletar informações sobre os vídeos de highlights de 2024.  
- Obter métricas como:
  - Visualizações
  - Curtidas
  - Comentários
  - Taxa de engajamento
- Atualizar automaticamente uma planilha no Google Sheets conectada ao **Looker Studio** para visualização dinâmica.

---

## Como rodar o projeto (Windows)

### 1. Clone o repositório

```bash
git clone https://github.com/lilicarla/f1-2024-highlights.git
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências do projeto

```bash
pip install google-api-python-client pandas gspread google-auth python-dotenv
```

### 4. Configure as credenciais do Google

#### 4.1 No Google Cloud Console, crie um projeto.
#### 4.2 Ative as APIs:
- YouTube Data API v3
- Google Sheets API
#### 4.3 Crie uma Service Account
#### 4.4 Baixe o arquivo de credenciais e renomeie para:
```bash
credentials.json
```
#### 4.5 Coloque o arquivo **credentials.json** na raiz do projeto
#### 4.6 Compartilhe a planilha do Google Sheets com o e-mail da service account

### 5. Configure as variáveis do projeto (.env)

```bash
PLAYLIST_ID = ""
SPREADSHEET_ID = ""
API_KEY = ""
```

### 6. Execute a pipeline

```bash
python main.py
```

---

## Links Importantes

📊 [Dashboard no Looker Studio](https://lookerstudio.google.com/reporting/022ffe58-3717-4b96-8dd0-767038757508)

🎞️ [Playlist 2024 F1 Race Highlights](https://youtube.com/playlist?list=PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR&si=4lzP0DEC-HoBZu4t)

