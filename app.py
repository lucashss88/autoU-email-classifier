import os
import json
from google import genai
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pypdf import PdfReader
from io import BytesIO

load_dotenv()

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    try:
        texto_email = request.form.get('texto_email', '')
        arquivo = request.files.get('arquivo_email')
        
        conteudo_final = ""

        if texto_email:
            conteudo_final = texto_email
        
        elif arquivo and allowed_file(arquivo.filename):
            filename = secure_filename(arquivo.filename)

            if filename.lower().endswith('.pdf'):
                try:
                    pdf_file = BytesIO(arquivo.read())
                    reader = PdfReader(pdf_file)
                    conteudo_final = "\n".join([page.extract_text() for page in reader.pages])
                except Exception as e:
                    return jsonify({'erro': 'O arquivo PDF está corrompido ou ilegível.'}), 400
            else:
                try:
                    conteudo_final = arquivo.read().decode('utf-8')
                except Exception as e:
                    return jsonify({'erro': 'O arquivo TXT está com encoding inválido. Use UTF-8.'}), 400
        else:
            return jsonify({'erro': 'Por favor, digite um texto ou envie um arquivo válido.'}), 400

        if not conteudo_final.strip():
            return jsonify({'erro': 'Não foi possível identificar texto no email enviado.'}), 400

        resultado = analisar_com_gemini(conteudo_final)
        return jsonify(resultado)

    except Exception as e:
        print(f"ERRO NO SERVIDOR: {e}")
        return jsonify({'erro': 'Ocorreu um erro interno. Verifique o terminal do Python.'}), 500

def analisar_com_gemini(texto):
    prompt = f"""
    Você é um assistente de triagem de emails para a empresa AutoU.
    Analise o seguinte email e classifique-o.
    
    Email:
    "{texto}"

    Regras:
    - Categoria "Produtivo": Solicitações, suporte, dúvidas, reclamações.
    - Categoria "Improdutivo": Agradecimentos, spam, felicitações, "ok", "obrigado".

    Responda EXATAMENTE neste formato JSON:
    {{
        "categoria": "Produtivo" ou "Improdutivo",
        "resposta_sugerida": "Escreva uma resposta curta e cordial aqui."
    }}
    """

    try:
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt,
            config={
                'response_mime_type': 'application/json'
            }
        )

        parsed_response = json.loads(response.text)
        return parsed_response

    except Exception as e:
        print(f"ERRO GEMINI: {e}")
        return {
            "categoria": "Erro na IA",
            "resposta_sugerida": "Não foi possível conectar ao Google Gemini. Verifique sua chave API."
        }

if __name__ == '__main__':
    app.run(debug=True)