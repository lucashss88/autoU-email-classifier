from pypdf import PdfReader
from io import BytesIO

ALLOWED_EXTENSIONS = {'txt', 'pdf'}


def validate_email_text(text: str) -> None:
    if not text or not text.strip():
        raise ValueError('Email text cannot be empty')


def validate_file_extension(filename: str) -> str:
    if '.' not in filename:
        raise ValueError('File has no extension')

    ext = filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f'File type not allowed. Use: {", ".join(ALLOWED_EXTENSIONS)}')

    return ext


def read_txt_file(content: bytes) -> str:
    try:
        return content.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError('TXT file has invalid encoding. Use UTF-8.')


def read_pdf_file(content: bytes) -> str:
    try:
        pdf_file = BytesIO(content)
        reader = PdfReader(pdf_file)
        texts = [page.extract_text() for page in reader.pages]
        return "\n".join([t or '' for t in texts])
    except Exception:
        raise ValueError('PDF file is corrupted or unreadable')


def process_file(filename: str, content: bytes) -> str:
    ext = validate_file_extension(filename)

    if ext == 'pdf':
        return read_pdf_file(content)
    return read_txt_file(content)
