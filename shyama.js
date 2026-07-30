// --- DOM Elements ---
const mobileMenu = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');
const navbar = document.querySelector('.navbar');
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;
const modal = document.getElementById('inquiryModal');
const modalProductName = document.getElementById('modalProductName');
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

// --- Mobile Menu Toggle ---
if (mobileMenu && navLinks) {
    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        // Prevent body scroll when menu is open
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : 'auto';
    });

    // Close mobile menu when a link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.style.overflow = 'auto';
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.navbar') && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
}

// --- Navbar Scroll Effect ---
let lastScroll = 0;
const scrollHandler = () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
};

window.addEventListener('scroll', scrollHandler);

// --- Dark Mode Logic (With Local Storage) ---
if (themeToggleBtn && themeIcon) {
    // Check user's previous preference
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'dark') {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        }
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // Auto-detect system preference
        document.documentElement.setAttribute('data-theme', 'dark');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }

    // Toggle Theme Function
    themeToggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        }
    });
}

// --- Intersection Observer for Scroll Animations ---
const animatedElements = document.querySelectorAll('.fade-in, .slide-up');

const appearanceOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
};

const appearanceObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        }
    });
}, appearanceOptions);

// Only observe elements that exist
if (animatedElements.length > 0) {
    animatedElements.forEach(element => {
        appearanceObserver.observe(element);
    });
}

// --- Active Nav Link Highlight Based on Scroll Position ---
const sections = document.querySelectorAll('section[id]');
const navItems = document.querySelectorAll('.nav-links a');

function highlightNavOnScroll() {
    let scrollPosition = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navItems.forEach(item => {
                item.classList.remove('active');
                if (item.getAttribute('href') === `#${sectionId}` || 
                    item.getAttribute('href') === `${sectionId}.html`) {
                    item.classList.add('active');
                }
            });
        }
    });
}

// Debounced scroll handler for better performance
const debouncedHighlightNav = debounce(highlightNavOnScroll, 10);
window.addEventListener('scroll', debouncedHighlightNav);

// --- Modal Inquiry Logic ---
function openModal(productName) {
    if (modal && modalProductName) {
        modal.classList.add('active');
        modalProductName.textContent = `Inquiring about: ${productName}`;
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
        
        // Focus first input in modal for better accessibility
        setTimeout(() => {
            const firstInput = modal.querySelector('input');
            if (firstInput) firstInput.focus();
        }, 100);
    }
}

function closeModal() {
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto'; // Restore scrolling
    }
}

// Close modal when clicking outside
if (modal) {
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
    
    // Trap focus within modal for accessibility
    modal.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
        // Tab trap
        if (e.key === 'Tab') {
            const focusableElements = modal.querySelectorAll('input, button, textarea');
            const firstElement = focusableElements[0];
            const lastElement = focusableElements[focusableElements.length - 1];
            
            if (e.shiftKey && document.activeElement === firstElement) {
                e.preventDefault();
                lastElement.focus();
            } else if (!e.shiftKey && document.activeElement === lastElement) {
                e.preventDefault();
                firstElement.focus();
            }
        }
    });
}

// Add event listeners to all "Inquire Now" buttons
document.querySelectorAll('.btn-secondary').forEach(button => {
    if (button.textContent.includes('Inquire Now')) {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const productCard = button.closest('.product-card');
            const productName = productCard.querySelector('h3').textContent;
            openModal(productName);
        });
    }
});

// --- Form Submissions Handling ---
async function handleFormSubmit(e) {
    e.preventDefault();
    
    if (!contactForm || !formStatus) return;

    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const company = document.getElementById('company').value.trim();
    const subject = document.getElementById('subject').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !subject || !message) {
        formStatus.textContent = 'Please fill in all required fields.';
        formStatus.style.color = '#e74c3c';
        formStatus.style.background = 'rgba(231, 76, 60, 0.1)';
        formStatus.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        formStatus.textContent = 'Please enter a valid email address.';
        formStatus.style.color = '#e74c3c';
        formStatus.style.background = 'rgba(231, 76, 60, 0.1)';
        formStatus.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        return;
    }

    // Show loading state
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.7';
    submitBtn.style.cursor = 'not-allowed';

    try {
        // Send data to backend API
        const response = await fetch('http://localhost:5000/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                email: email,
                company: company,
                subject: subject,
                message: message
            })
        });

        const result = await response.json();

        if (result.success) {
            formStatus.textContent = result.message;
            formStatus.style.color = '#27ae60';
            formStatus.style.background = 'rgba(39, 174, 96, 0.1)';
            contactForm.reset();
        } else {
            formStatus.textContent = result.message || 'Error sending message. Please try again.';
            formStatus.style.color = '#e74c3c';
            formStatus.style.background = 'rgba(231, 76, 60, 0.1)';
        }
    } catch (error) {
        formStatus.textContent = 'Error sending message. Please try again or contact us directly at info@shyamaengineering.com';
        formStatus.style.color = '#e74c3c';
        formStatus.style.background = 'rgba(231, 76, 60, 0.1)';
        console.error('Form submission error:', error);
    } finally {
        // Reset button state
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
        submitBtn.style.opacity = '1';
        submitBtn.style.cursor = 'pointer';

        // Clear message after 5 seconds
        setTimeout(() => {
            formStatus.textContent = '';
        }, 5000);
    }
}

function handleModalSubmit(e) {
    e.preventDefault();
    
    const modalForm = e.target;
    const modalName = document.getElementById('modalName').value.trim();
    const modalEmail = document.getElementById('modalEmail').value.trim();
    const modalRequirements = document.getElementById('modalRequirements').value.trim();

    // Basic validation
    if (!modalName || !modalEmail || !modalRequirements) {
        alert('Please fill in all required fields.');
        return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(modalEmail)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Simulate submission
    const submitBtn = modalForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.7';
    submitBtn.style.cursor = 'not-allowed';

    setTimeout(() => {
        alert('✓ Thank you for your inquiry! Our team will contact you within 24 hours.');
        modalForm.reset();
        closeModal();
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
        submitBtn.style.opacity = '1';
        submitBtn.style.cursor = 'pointer';
    }, 1500);
}

// Add form submit listeners
if (contactForm) {
    contactForm.addEventListener('submit', handleFormSubmit);
}

// Add modal form submit listener
const modalForm = document.querySelector('#inquiryModal form');
if (modalForm) {
    modalForm.addEventListener('submit', handleModalSubmit);
}

// --- Counter Animation for Hero Stats ---
function animateCounters() {
    const counters = document.querySelectorAll('.stat-item h3');
    
    counters.forEach(counter => {
        const target = parseInt(counter.textContent);
        const suffix = counter.textContent.replace(/[0-9]/g, '');
        let current = 0;
        const increment = target / 50;
        const duration = 2000; // 2 seconds
        const stepTime = duration / 50;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.textContent = target + suffix;
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current) + suffix;
            }
        }, stepTime);
    });
}

// Trigger counter animation when hero section is visible
const heroSection = document.querySelector('.hero');
if (heroSection) {
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counterObserver.observe(heroSection);
}

// --- Smooth Scroll for Anchor Links ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const navbarHeight = navbar.offsetHeight;
            const targetPosition = targetElement.offsetTop - navbarHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// --- Phone Number Link Enhancement ---
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    link.addEventListener('click', function(e) {
        // On mobile, this will open the phone app
        // On desktop, it's a clickable link
        console.log('Phone number clicked:', this.textContent);
    });
});

// --- Email Link Enhancement ---
document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
    link.addEventListener('click', function(e) {
        console.log('Email clicked:', this.textContent);
    });
});

// --- Lazy Loading for Images (Performance Optimization) ---
if ('loading' in HTMLImageElement.prototype) {
    // Native lazy loading supported
    document.querySelectorAll('img').forEach(img => {
        img.loading = 'lazy';
    });
} else {
    // Fallback for browsers that don't support native lazy loading
    const lazyImages = document.querySelectorAll('img');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
}

// --- Form Input Enhancements ---
// Add floating label effect
document.querySelectorAll('.contact-form input, .contact-form textarea').forEach(input => {
    input.addEventListener('focus', () => {
        input.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', () => {
        if (!input.value) {
            input.parentElement.classList.remove('focused');
        }
    });
});

// --- Performance: Debounce Scroll Events ---
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// --- Initialize on DOM Load ---
document.addEventListener('DOMContentLoaded', () => {
    // Add loaded class to body for initial animations
    document.body.classList.add('loaded');
    
    // Trigger initial nav highlight
    highlightNavOnScroll();
    
    // Log initialization
    console.log('Shyama Engineering - Website Initialized');
    console.log('Features: Mobile Menu, Dark Mode, Scroll Animations, Form Validation, Modal System');
    
    // Add touch event optimizations for mobile
    if ('ontouchstart' in window) {
        document.body.classList.add('touch-device');
        
        // Improve touch scrolling performance
        document.querySelectorAll('.hero-stats, .product-card, .service-box').forEach(el => {
            el.style.transform = 'translateZ(0)';
        });
    }
    
    // Detect mobile device
    const isMobile = window.innerWidth <= 768;
    if (isMobile) {
        document.body.classList.add('mobile-device');
    }
    
    // Handle orientation change on mobile
    window.addEventListener('orientationchange', () => {
        setTimeout(() => {
            window.scrollTo(0, window.scrollY);
            highlightNavOnScroll();
        }, 100);
    });
    
    // Resize handler for responsive adjustments
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            // Close mobile menu on resize to desktop
            if (window.innerWidth > 768 && navLinks && mobileMenu) {
                navLinks.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
            
            // Update mobile class
            if (window.innerWidth <= 768) {
                document.body.classList.add('mobile-device');
            } else {
                document.body.classList.remove('mobile-device');
            }
            
            highlightNavOnScroll();
        }, 250);
    });
});

// --- Error Handling ---
window.addEventListener('error', (e) => {
    console.error('Website Error:', e.message);
    // You can add error reporting here
});

// --- Network Status Detection ---
window.addEventListener('online', () => {
    console.log('Connection restored');
});

window.addEventListener('offline', () => {
    console.log('Connection lost - Some features may be limited');
});

// --- Prevent zoom on double tap for mobile (optional) ---
let lastTouchEnd = 0;
document.addEventListener('touchend', (event) => {
    const now = Date.now();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, { passive: false });

// --- Service Worker Registration (for PWA capabilities) ---
if ('serviceWorker' in navigator) {
    // Uncomment when service worker is ready
    // navigator.serviceWorker.register('/sw.js')
    //     .then(reg => console.log('Service Worker registered'))
    //     .catch(err => console.error('Service Worker registration failed:', err));
}

// --- Export functions for global access (if needed) ---
window.openModal = openModal;
window.closeModal = closeModal;
window.handleFormSubmit = handleFormSubmit;
window.handleModalSubmit = handleModalSubmit;