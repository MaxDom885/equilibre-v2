// Initialisation contrôlée pour éviter les conflits
document.addEventListener('DOMContentLoaded', () => {
    // 1. Configuration du carousel Swiper
    const initServicesCarousel = () => {
        new Swiper('.services-carousel', {
            loop: true,
            slidesPerView: 1,
            spaceBetween: 30,
            speed: 800,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: { slidesPerView: 2 },
                1024: { 
                    slidesPerView: 3,
                    spaceBetween: 40,
                },
                1440: { 
                    slidesPerView: 4,
                    spaceBetween: 50,
                }
            },
            on: {
                init: function () {
                    this.slides.forEach(slide => {
                        slide.style.transition = 'opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
                    });
                },
            },
        });
    };

    // 2. Animations au défilement
    const animateOnScroll = () => {
        // Animation des éléments généraux
        const elements = document.querySelectorAll('.animate-on-scroll');
        const animationOptions = {
            threshold: 0.2,
            rootMargin: '0px 0px -20% 0px'
        };

        const generalObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, animationOptions);

        elements.forEach(element => generalObserver.observe(element));

        // Animation spécifique pour les images
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active-image');
                }
            });
        }, { threshold: 0.2 });

        document.querySelectorAll('.service-detail-page img:not(.service-header img)').forEach(img => {
            imageObserver.observe(img);
        });
    };

    // 3. Initialisation conditionnelle
    if (document.querySelector('.services-carousel')) {
        initServicesCarousel();
        animateOnScroll();
    }

    // 4. Optimisations des performances
    window.addEventListener('scroll', () => {
        requestAnimationFrame(animateOnScroll);
    }, { passive: true });
});

const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('.animate-on-scroll').forEach(section => {
    section.style.animationPlayState = 'paused';
    sectionObserver.observe(section);
});

document.addEventListener('DOMContentLoaded', () => {
    // 1. Déclaration des keyframes manquantes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes popIn {
            from { opacity: 0; transform: scale(0.95) translateY(20px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }
    `;
    document.head.appendChild(style);

    // 2. Configuration de l'observateur dans la bonne portée
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
                entry.target.style.transform = 'translateZ(0)';
            }
        });
    }, { 
        threshold: 0.25,
        rootMargin: '0px 0px -150px 0px'
    });

    // 3. Application aux éléments après vérification
    document.querySelectorAll('.animate-on-scroll').forEach(section => {
        if (section) {
            section.style.animationPlayState = 'paused';
            section.style.willChange = 'opacity, transform'; // Optimisation
            sectionObserver.observe(section);
        }
    });

    // 4. Animation popIn avec vérification
    document.querySelectorAll('.animate-pop-in').forEach((el, index) => {
        if (el) {
            el.style.animation = `popIn 0.8s cubic-bezier(0.22, 1, 0.36, 1) ${index * 0.15}s forwards`;
            el.style.opacity = '0'; // État initial
        }
    });
});

// Animation des cartes au scroll
document.addEventListener('DOMContentLoaded', () => {
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0) rotateX(0)';
            }
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('.service-card').forEach(card => {
        cardObserver.observe(card);
    });

    // Effet parallaxe au survol
    document.querySelectorAll('.service-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            
            card.style.transform = `
                perspective(1000px)
                rotateX(${y * 8}deg)
                rotateY(${x * 8}deg)
                translateZ(20px)
            `;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
        });
    });
});