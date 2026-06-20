document.addEventListener('DOMContentLoaded', function() {
    var accordions = document.querySelectorAll('.faq-accordion');
    accordions.forEach(function(el) {
        el.addEventListener('click', function(e) {
            if (!e.target.closest('.faq-accordion_control')) return;

            var self = this;
            var control = self.querySelector('.faq-accordion_control');
            var content = self.querySelector('.faq-accordion_content');

            self.classList.toggle('open');

            if (self.classList.contains('open')) {
                content.style.maxHeight = content.scrollHeight + 'px';
            } else {
                content.style.maxHeight = null;
            }
        });
    });
});




document.addEventListener('DOMContentLoaded', function() {
  const steps = document.querySelectorAll('.step');
  let currentStep = 0;

  if (steps.length > 0) {
    steps[0].classList.add('active');
  }

  function nextStep() {
    if (currentStep < steps.length - 1) {
      steps[currentStep].classList.remove('active');
      currentStep++;
      steps[currentStep].classList.add('active');
    }
  }

  document.querySelectorAll('.quiz_button').forEach(btn => {
    btn.addEventListener('click', nextStep);
  });
});