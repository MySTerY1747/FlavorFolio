document.addEventListener('DOMContentLoaded', function () {
  formatTextBlocks('.ingredients-box');
  formatTextBlocks('.instructions-box');

  function formatTextBlocks(selector) {
    document.querySelectorAll(selector).forEach(box => {
      // Preserve newlines and convert to paragraphs
      const content = box.innerHTML.replace(/\n/g, '</p><p>');
      box.innerHTML = `<p>${content}</p>`;

      // Remove empty paragraphs
      Array.from(box.getElementsByTagName('p')).forEach(p => {
        if (p.textContent.trim() === '') p.remove();
      });
    });
  }
});
