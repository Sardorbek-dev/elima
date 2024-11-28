const navbarCollapseBase = document.getElementById('navbarsExample11');
const navbarToggler = document.querySelector('.navbar-toggler');

// When the menu is fully shown, slide in both the menu and background
navbarCollapseBase.addEventListener('shown.bs.collapse', function () {
document.body.classList.add('expand');
    setTimeout(() => {
        document.body.classList.add('expand-active');
    }, 10); // Slight delay for smooth transition
    });

    // When the menu is about to hide, we trigger the sliding-out effect
    navbarCollapseBase.addEventListener('hide.bs.collapse', function (e) {
    e.preventDefault(); // Prevent Bootstrap from removing the 'show' class immediately

    // Add the sliding-out class to animate it out
    navbarCollapseBase.classList.add('sliding-out');
    document.body.classList.remove('expand-active'); // Start sliding the background out

    setTimeout(() => {
        navbarCollapseBase.classList.remove('show'); // After slide-out animation, remove the 'show' class
        navbarCollapseBase.classList.remove('sliding-out'); // Remove sliding-out class after animation
        document.body.classList.remove('expand'); // Finally, remove expand class
    }, 500); // Duration matches the CSS transition (0.5s)
});

const counters = document.querySelectorAll('.elima-statistics');

counters.forEach(counter => {
    const animate = () => {
        const target = +counter.getAttribute('counter-animation');
        const current = +counter.innerText;

        // Determine the increment based on the target value
        let increment;
        if (target < 50) {
            increment = target / 100; // Slower for small numbers
        } else if (target < 100) {
            increment = target / 50;  // Medium speed for moderate numbers
        } else {
            increment = target / 20;  // Faster for large numbers
        }

        if (current < target) {
            counter.innerText = Math.ceil(current + increment);
            setTimeout(animate, 50); // Add a delay between increments for a slower effect
        } else {
            counter.innerText = target;
        }
    };
    animate();
});

document.addEventListener('DOMContentLoaded', function () {
    const accordionItems = document.querySelectorAll('.accordion-item-hover');
    const accordions = document.querySelectorAll('.accordion-collapse');

    // Add hover functionality to each accordion item
    accordionItems.forEach((item) => {
        item.addEventListener('mouseover', () => {
            // Close all other accordion items and remove the background-color-hovered class
            accordionItems.forEach((otherItem) => {
                const collapse = otherItem.querySelector('.accordion-collapse');
                if (collapse && collapse !== item.querySelector('.accordion-collapse')) {
                    collapse.classList.remove('show');
                }
                otherItem.classList.remove('background-color-hovered');
            });

            // Open the hovered accordion item
            const collapseTarget = item.querySelector('.accordion-collapse');
            if (collapseTarget) {
                collapseTarget.classList.add('show');
            }

            // Add the background-color-hovered class to the hovered accordion item
            item.classList.add('background-color-hovered');
        });
    });
});

