// --- Mobile Menu Toggle ---
const mobileMenu = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');

mobileMenu.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});


// --- Dark Mode Logic (With Local Storage) ---
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = themeToggleBtn.querySelector('i');

// Check user's previous preference
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }
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


// --- Intersection Observer for Scroll Animations ---
const animatedElements = document.querySelectorAll('.fade-in, .slide-up');

const appearanceOptions = {
    threshold: 0.15, // Triggers when 15% of the element is visible
    rootMargin: "0px 0px -50px 0px"
};

const appearanceObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('appear');
            // Once it appears, stop observing to improve performance
            observer.unobserve(entry.target);
        }
    });
}, appearanceOptions);

animatedElements.forEach(element => {
    appearanceObserver.observe(element);
});


// --- Active Nav Link Highlight Based on Current Page ---
const navItems = document.querySelectorAll('.nav-links a');
const currentPage = window.location.pathname;

navItems.forEach(item => {
    item.classList.remove('active');
    if (item.getAttribute('href') === currentPage || 
        (currentPage.endsWith('/') && item.getAttribute('href') === 'index.html')) {
        item.classList.add('active');
    }
});


// --- Modal Inquiry Logic ---
const modal = document.getElementById('inquiryModal');
const modalProductName = document.getElementById('modalProductName');

function openModal(productName) {
    modal.style.display = 'flex';
    modalProductName.textContent = `Inquiring about: ${productName}`;
}

function closeModal() {
    modal.style.display = 'none';
}

window.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});


// --- Form Submissions Handling ---
function handleFormSubmit(e) {
    e.preventDefault();
    const status = document.getElementById('formStatus');
    status.textContent = "Thank you! Your message has been sent successfully.";
    document.getElementById('contactForm').reset();
    setTimeout(() => { status.textContent = ""; }, 4000);
}

function handleModalSubmit(e) {
    e.preventDefault();
    alert('Thank you! Your product inquiry has been submitted.');
    closeModal();
}
