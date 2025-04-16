/**
 * Initialisation des animations de compteurs
 */
function initCounters() {
    const counterElements = document.querySelectorAll('[data-target]');
    if (!counterElements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    });

    function animateCounter(counter) {
        const target = +counter.dataset.target;
        const prefix = counter.dataset.prefix || '';
        const suffix = counter.dataset.suffix || '';
        const duration = 2000;
        const startTime = Date.now();

        const updateCounter = () => {
            const progress = Math.min((Date.now() - startTime) / duration, 1);
            counter.textContent = prefix + Math.floor(progress * target) + suffix;
            if (progress < 1) requestAnimationFrame(updateCounter);
        };

        requestAnimationFrame(updateCounter);
    }

    counterElements.forEach(counter => observer.observe(counter));
}

/**
 * Initialisation des carousels Bootstrap
 */
function initCarousels() {
    document.querySelectorAll('.carousel').forEach(carousel => {
        new bootstrap.Carousel(carousel, {
            interval: carousel.id === 'partnersCarousel' ? 3000 : 5000,
            wrap: true,
            touch: true,
            keyboard: true,
            pause: carousel.id === 'partnersCarousel' ? 'hover' : false
        });
    });
}

/**
 * Initialisation du slider Swiper pour les partenaires
 */
function initPartnersSlider() {
    const swiperEl = document.querySelector('.partnersSwiper');
    if (!swiperEl) return;

    new Swiper(swiperEl, {
        loop: true,
        autoplay: {
            delay: 2000,
            disableOnInteraction: false,
        },
        slidesPerView: 'auto', // Permet un nombre variable de slides
        centeredSlides: false,
        spaceBetween: 15, // Espacement réduit sur tous les écrans
        keyboard: { enabled: true },
        breakpoints: {
            // Configuration responsive révisée :
            400: {  // À partir de 400px de large
                spaceBetween: 20
            },
            576: {
                slidesPerView: 3,
                spaceBetween: 20
            },
            768: {
                slidesPerView: 4,
                spaceBetween: 25
            },
            992: {
                slidesPerView: 5,
                spaceBetween: 30
            },
            1200: {
                slidesPerView: 6,
                spaceBetween: 40
            }
        }
    });
}

/**
 * Gestion des dropdowns avec hover sur desktop
 */
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.dropdown-hover');
    if (!dropdowns.length) return;

    function setupDropdown(dropdown) {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        const menu = dropdown.querySelector('.dropdown-menu');
        const isDesktop = window.matchMedia('(min-width: 992px)').matches;

        if (isDesktop) {
            dropdown.addEventListener('mouseenter', () => showMenu(menu));
            dropdown.addEventListener('mouseleave', () => hideMenu(menu));
        } else {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                menu.classList.toggle('show');
            });
        }
    }

    function showMenu(menu) {
        menu.style.display = 'block';
        setTimeout(() => menu.classList.add('show'), 10);
    }

    function hideMenu(menu) {
        menu.classList.remove('show');
        setTimeout(() => {
            if (!menu.classList.contains('show')) {
                menu.style.display = 'none';
            }
        }, 300);
    }

    dropdowns.forEach(setupDropdown);

    // Réinitialisation au redimensionnement
    window.addEventListener('resize', () => {
        dropdowns.forEach(dropdown => {
            const menu = dropdown.querySelector('.dropdown-menu');
            menu.removeAttribute('style');
            menu.classList.remove('show');
        });
        dropdowns.forEach(setupDropdown);
    });
}

/**
 * Marquage de la page active dans la navigation
 */
function initActivePage() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || 
            (currentPath === '/' && linkPath === '/') || 
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });
}

/**
 * Initialisation globale
 */
function initAll() {
    initCounters();
    initCarousels();
    initDropdowns();
    initActivePage();
    initPartnersSlider();

    // Animation navbar au scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });
    }
}

// Lancement
if (document.readyState === 'complete') {
    initAll();
} else {
    document.addEventListener('DOMContentLoaded', initAll);
}