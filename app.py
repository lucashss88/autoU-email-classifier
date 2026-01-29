import logging
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from services.simple_validators import validate_email_text, process_file
from services.simple_ai import analyze_with_gemini

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    try:
        email_text = request.form.get('email_text', '').strip()
        arquivo = request.files.get('email_file')

        conteudo_final = ''

        if email_text:
            validate_email_text(email_text)
            conteudo_final = email_text

        elif arquivo and arquivo.filename:
            filename = secure_filename(arquivo.filename)
            conteudo_final = process_file(filename, arquivo.read())

        else:
            return jsonify({'erro': 'Por favor, digite um texto ou envie um arquivo válido.'}), 400

        validate_email_text(conteudo_final)

        result = analyze_with_gemini(conteudo_final)
        return jsonify(result)

    except ValueError as e:
        logger.warning(f"Validation failed: {e}")
        return jsonify({'error': str(e)}), 400

    except Exception as e:
        logger.error(f"SERVER ERROR: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error. Check the Python terminal.'}), 500

if __name__ == '__main__':
    app.run(debug=True)