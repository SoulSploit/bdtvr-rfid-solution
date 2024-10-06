// Wait for the DOM to fully load before executing scripts
document.addEventListener("DOMContentLoaded", function () {
    console.log("BDT&VR RFID Solution scripts initialized.");

    // Smooth scrolling for navigation links
    setupSmoothScrolling();

    // Show a welcome message on page load
    showTemporaryMessage("Welcome to BDT&VR! Explore our RFID solutions.", 5000);

    // Fetch and populate data (uncomment to use)
    // fetchDataAndPopulate();

    // Initialize tooltips (if using)
    setupTooltips();
});

// Function to set up smooth scrolling
function setupSmoothScrolling() {
    const links = document.querySelectorAll('nav ul li a');

    links.forEach(link => {
        link.addEventListener('click', function (event) {
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                event.preventDefault(); // Prevent default anchor click behavior
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Function to show a temporary message with fade-out effect
function showTemporaryMessage(message, duration = 5000) {
    const messageDiv = document.createElement('div');
    messageDiv.innerText = message;
    messageDiv.className = 'temporary-message';
    document.body.appendChild(messageDiv);

    // Automatically hide the message after the specified duration
    setTimeout(() => {
        messageDiv.style.opacity = '0'; // Fade out
        setTimeout(() => messageDiv.remove(), 500); // Remove after fade out
    }, duration);
}

// Async function to fetch data and populate a section
async function fetchDataAndPopulate() {
    try {
        const response = await fetch('/api/data'); // Adjust endpoint as necessary
        if (!response.ok) throw new Error("Network response was not ok");
        const data = await response.json();

        // Process and display data (example logic)
        const dataContainer = document.getElementById('data-container'); // Example container
        dataContainer.innerHTML = ""; // Clear previous data

        data.forEach(item => {
            const div = document.createElement('div');
            div.className = 'data-item';
            div.innerHTML = `<h3>${item.title}</h3><p>${item.description}</p>`;
            dataContainer.appendChild(div);
        });
    } catch (error) {
        console.error("Failed to fetch data:", error);
        showTemporaryMessage("Failed to load data. Please try again later.");
    }
}

// Function to initialize tooltips (if using)
function setupTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');

    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function () {
            const tooltipText = this.getAttribute('data-tooltip');
            const tooltipDiv = document.createElement('div');
            tooltipDiv.className = 'tooltip';
            tooltipDiv.innerText = tooltipText;
            document.body.appendChild(tooltipDiv);

            const rect = this.getBoundingClientRect();
            tooltipDiv.style.left = `${rect.left + window.scrollX}px`;
            tooltipDiv.style.top = `${rect.bottom + window.scrollY + 5}px`; // Position below the element

            // Remove tooltip on mouse leave
            this.addEventListener('mouseleave', function () {
                tooltipDiv.remove();
            });
        });
    });
}
