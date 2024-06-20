document.querySelectorAll('.clickable').forEach(section => {
    section.addEventListener('click', function() {
        const link = this.getAttribute('data-link');
        window.location.href = link;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section');
    const currentScroll = window.scrollY + window.innerHeight / 2;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;

        if (currentScroll >= sectionTop && currentScroll < sectionTop + sectionHeight) {
            document.body.style.background = section.style.background;
        }
    });
});
