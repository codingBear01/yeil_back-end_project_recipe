document.addEventListener('DOMContentLoaded', () => {
  const video = document.querySelectorAll('.video');

  video.forEach((el) => {
    el.innerHTML = el.getAttribute('value');
  });
});
