const form = document.getElementById('form-upload');
const resultArea = document.getElementById('resultado-area');
const loading = document.getElementById('loading');
const categoriaBadge = document.getElementById('res-categoria');
const respostaBox = document.getElementById('res-resposta');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    loading.style.display = 'flex';
    resultArea.style.display = 'none';

    const formData = new FormData(form);

    try {
        const response = await fetch('/processar', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.erro || 'Erro desconhecido no servidor');
        }

        const data = await response.json();
        console.log(data);

        categoriaBadge.innerText = data.categoria;
        respostaBox.value = data.resposta_sugerida;

        resultArea.className = 'card card-result shadow-sm p-4 mt-4';
        if (data.categoria === 'Produtivo') {
            categoriaBadge.className = 'badge bg-success fs-5';
            resultArea.classList.add('produtivo');
        } else {
            categoriaBadge.className = 'badge bg-warning text-dark fs-5';
            resultArea.classList.add('improdutivo');
        } 

        resultArea.style.display = 'block';
    } catch (error) {
        alert('Erro ao processar o arquivo. Tente novamente.');
        console.error('Error:', error);
    } finally {
        loading.style.display = 'none';
    }
});