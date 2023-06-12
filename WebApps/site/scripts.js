document.addEventListener('DOMContentLoaded', function () {
  const images = document.querySelectorAll('.audio-container img');

  images.forEach(img => {
    img.addEventListener('click', function () {
      const audio = img.nextElementSibling;
      if (audio.paused) {
        audio.play();
      } else {
        audio.pause();
      }
    });
  });
});

// Smooth scrolling and animations
document.addEventListener('DOMContentLoaded', function () {
  // Smooth scrolling
  const navLinks = document.querySelectorAll('nav a');
  navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      target.scrollIntoView({ behavior: 'smooth' });
    });
  });

  // IntersectionObserver for animations
  const sections = document.querySelectorAll('.welcome-section, .about-section, .contact-section');
  const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'fadeIn 2s ease';
      } else {
        entry.target.style.animation = 'none';
      }
    });
  }, options);

  sections.forEach(section => {
    observer.observe(section);
  });
});
