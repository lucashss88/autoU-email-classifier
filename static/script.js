import { analyze } from './js/apiClient.js';
import { setupInputToggles, validateForm } from './js/validation.js';
import { showLoading, hideLoading, renderResult } from './js/ui.js';

const form = document.getElementById('upload-form');
const resultArea = document.getElementById('result-area');
const loading = document.getElementById('loading');
const categoryBadge = document.getElementById('res-category');
const responseBox = document.getElementById('res-response');
const emailText = document.querySelector('textarea[name="email_text"]');
const emailFile = document.querySelector('input[name="email_file"]');
const btnAnalyze = document.getElementById('btn-analyze');

setupInputToggles({ emailTextEl: emailText, emailFileEl: emailFile, validate: () => validateForm({ emailTextEl: emailText, emailFileEl: emailFile, submitBtn: btnAnalyze }) });

validateForm({ emailTextEl: emailText, emailFileEl: emailFile, submitBtn: btnAnalyze });

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  showLoading(loading);
  resultArea.style.display = 'none';

  const formData = new FormData(form);

  try {
    const data = await analyze(formData);
    renderResult(resultArea, categoryBadge, responseBox, data);
  } catch (error) {
    alert('Error processing the file. Please try again.');
    console.error('Error:', error);
  } finally {
    hideLoading(loading);
  }
});
