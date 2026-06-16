var accordions = document.querySelectorAll('.faq-accordion');
accordions.forEach(function (el) {
  el.addEventListener('click', function (e) {
    var self = e.currentTarget;
    var control = self.querySelector('.faq-accordion_control');
    var content = self.querySelector('.faq-accordion_content');
    self.classList.toggle('open'); // если открыт аккордеон

    if (self.classList.contains('open')) {
      control.setAttribute('aria-expanded', true);
      content.setAttribute('aria-hidden', false);
      content.style.maxHeight = content.scrollHeight + 'px';
    } else {
      control.setAttribute('aria-expanded', false);
      content.setAttribute('aria-hidden', true);
      content.style.maxHeight = null;
    }
  });
});