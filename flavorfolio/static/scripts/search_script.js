// Tag input handling
document.getElementById('tagInput').addEventListener('keydown', function (e) {
  if (e.key === 'Enter') {
    e.preventDefault();
    const rawValue = this.value.trim();
    if (rawValue !== '') {
      addTag(rawValue);
      this.value = '';
    }
  }
});

// Tag removal handling
document.getElementById('tagContainer').addEventListener('click', function (e) {
  if (e.target.classList.contains('btn-close')) {
    e.preventDefault();
    const tagName = e.target.getAttribute('data-tag');
    removeTag(tagName);
    e.target.closest('.badge').remove();
    document.getElementById('searchForm').submit();
  }
});

// Tag case normalization
function normalizeTagCase(tagName) {
  return tagName.trim()
    .toLowerCase()
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

// Add tag function
function addTag(rawTagName) {
  const tagName = normalizeTagCase(rawTagName);
  const tagContainer = document.getElementById('tagContainer');
  const hiddenTagsContainer = document.getElementById('hiddenTagsContainer');

  // Check for duplicates
  const existingTags = Array.from(hiddenTagsContainer.querySelectorAll('input[name="tags"]'))
    .map(input => input.value);
  if (existingTags.includes(tagName)) return;

  // Add hidden input
  const hiddenInput = document.createElement('input');
  hiddenInput.type = 'hidden';
  hiddenInput.name = 'tags';
  hiddenInput.value = tagName;
  hiddenTagsContainer.appendChild(hiddenInput);

  // Add visible pill
  const pill = document.createElement('span');
  pill.className = 'badge bg-primary rounded-pill d-inline-flex align-items-center me-2 fs-6';
  pill.innerHTML = `
        ${tagName}
        <button 
            type="button" 
            class="btn-close btn-close-white ms-2" 
            aria-label="Remove"
            data-tag="${tagName}"
        ></button>
    `;
  tagContainer.appendChild(pill);
}

// Remove tag function
function removeTag(tagName) {
  const hiddenTagsContainer = document.getElementById('hiddenTagsContainer');
  const inputs = hiddenTagsContainer.querySelectorAll('input[name="tags"]');

  inputs.forEach(input => {
    if (input.value === tagName) {
      input.remove();
    }
  });
}

// Datalist visibility control
document.getElementById('tagInput').addEventListener('input', function (e) {
  const list = document.getElementById('tagSuggestions');
  list.style.display = this.value.trim() ? 'block' : 'none';
});

document.getElementById('tagInput').addEventListener('blur', function () {
  setTimeout(() => {
    document.getElementById('tagSuggestions').style.display = 'none';
  }, 200);
});

document.getElementById('tagInput').addEventListener('input', function (e) {
  const list = document.getElementById('tagSuggestions');
  list.style.display = this.value.trim() ? 'block' : 'none';
});

document.getElementById('tagInput').addEventListener('blur', function () {
  setTimeout(() => {
    document.getElementById('tagSuggestions').style.display = 'none';
  }, 200);
});
