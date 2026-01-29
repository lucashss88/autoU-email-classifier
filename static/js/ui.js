export function showLoading(el) {
  el.style.display = 'flex';
}

export function hideLoading(el) {
  el.style.display = 'none';
}

export function renderResult(elResult, badgeEl, responseEl, data) {
  badgeEl.innerText = data.category || '';
  responseEl.value = data.suggested_response || '';

  elResult.className = 'card card-result shadow-sm p-4 mt-4';
  elResult.classList.remove('productive', 'unproductive');

  if (data.category === 'Produtivo') {
    badgeEl.className = 'badge bg-success fs-5';
    elResult.classList.add('productive');
  } else {
    badgeEl.className = 'badge bg-warning text-dark fs-5';
    elResult.classList.add('unproductive');
  }

  elResult.style.display = 'block';
}
