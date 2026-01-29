export async function analyze(formData) {
  const response = await fetch('/processar', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    let err = { error: 'Unknown server error' };
    try {
      err = await response.json();
    } catch (_) {}
    throw new Error(err.error || 'Unknown server error');
  }

  return response.json();
}
