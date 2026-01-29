export function setupInputToggles({ emailTextEl, emailFileEl, validate }) {
  emailFileEl.addEventListener('change', () => {
    if (emailFileEl.files.length > 0) {
      emailTextEl.disabled = true;
      emailTextEl.value = '';
      emailTextEl.style.opacity = '0.5';
      emailTextEl.style.cursor = 'not-allowed';
    } else {
      emailTextEl.disabled = false;
      emailTextEl.style.opacity = '1';
      emailTextEl.style.cursor = 'auto';
    }
    validate();
  });

  emailTextEl.addEventListener('input', () => {
    if (emailTextEl.value.trim().length > 0) {
      emailFileEl.disabled = true;
      emailFileEl.value = '';
      emailFileEl.style.opacity = '0.5';
      emailFileEl.style.cursor = 'not-allowed';
    } else {
      emailFileEl.disabled = false;
      emailFileEl.style.opacity = '1';
      emailFileEl.style.cursor = 'auto';
    }
    validate();
  });
}

export function validateForm({ emailTextEl, emailFileEl, submitBtn }) {
  const hasText = emailTextEl.value.trim().length > 0;
  const hasFile = emailFileEl.files.length > 0;
  submitBtn.disabled = !(hasText || hasFile);
}
