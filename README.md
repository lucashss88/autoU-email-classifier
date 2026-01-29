# AutoU - Classificador Inteligente de Emails

> Solução desenvolvida para o Desafio Técnico da AutoU.

Uma aplicação web full-stack que utiliza Inteligência Artificial (**Google Gemini 1.5 Flash**) para automatizar a triagem de emails corporativos. O sistema lê arquivos (.txt, .pdf) ou texto inserido manualmente, classifica a mensagem como **Produtiva** ou **Improdutiva** e sugere uma resposta automática adequada.

---

## 🔗 Links do Projeto

- **Aplicação Online (Deploy):** https://autouemailclassifier.vercel.app/

---

## 🚀 Funcionalidades

- **Upload de Arquivos:** Suporte para leitura automática de arquivos `.txt` e `.pdf`.
- **Entrada Manual:** Campo de texto para colagem direta do corpo do email.
- **IA Generativa:** Integração com **Google Gemini 3 Preview** para análise semântica e contextual.
- **Classificação Automática:**
  - 🟢 **Produtivo:** Solicitações de suporte, dúvidas técnicas, status de chamados.
  - 🟡 **Improdutivo:** Agradecimentos, spam, felicitações, mensagens sem ação necessária.
- **Sugestão de Resposta:** Geração automática de uma resposta cordial e contextualizada.
- **Interface Responsiva:** Frontend limpo e moderno utilizando Bootstrap 5.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Flask.
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API), Bootstrap 5.
- **IA/LLM:** Google Gemini API (Modelo `gemini-3-flash-preview`).
- **Manipulação de Arquivos:** PyPDF (para leitura de PDFs).
- **Deploy:** Vercel (Serverless Functions).

---

## 💻 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar a aplicação na sua máquina.

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Uma chave de API do Google AI Studio (Gratuita).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/lucashss88/autoU-email-classifier
   cd NOME-DO-REPO
   ```
2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure a variável de ambiente para a API Key:**
   Crie um arquivo chamado .env na raiz do projeto, e adicione sua chave do google gemini neste formato.
   ```bash
   GEMINI_API_KEY=Cole_Sua_Chave_Aqui
   ```
4. **Execute a aplicação:**
   ```bash
    python app.py
   ```
