/**
 * Login Page with XSS Vulnerabilities
 * WARNING: This code contains intentional vulnerabilities for testing purposes
 */

// VULNERABILITY: XSS - Direct DOM manipulation with user input
function displayWelcomeMessage(username) {
    // VULNERABLE: Direct innerHTML assignment
    document.getElementById('welcome').innerHTML = `Welcome, ${username}!`;
}

// VULNERABILITY: XSS - Unsanitized URL parameters
function showError() {
    const urlParams = new URLSearchParams(window.location.search);
    const error = urlParams.get('error');
    
    // VULNERABLE: Direct HTML injection
    document.body.innerHTML += `<div class="error">${error}</div>`;
}

// VULNERABILITY: XSS - eval() with user input
function processUserInput(input) {
    // VULNERABLE: Using eval() with user input
    eval(`console.log("User input: ${input}")`);
}

// VULNERABILITY: XSS - document.write with user data
function renderUserProfile(userData) {
    // VULNERABLE: document.write with unsanitized data
    document.write(`
        <h1>${userData.name}</h1>
        <p>Email: ${userData.email}</p>
        <p>Bio: ${userData.bio}</p>
    `);
}

// VULNERABILITY: XSS - innerHTML with user-controlled data
function updateProfile(data) {
    const profileDiv = document.getElementById('profile');
    // VULNERABLE: No sanitization
    profileDiv.innerHTML = `
        <div class="profile">
            <h2>${data.username}</h2>
            <p>${data.description}</p>
        </div>
    `;
}

// VULNERABILITY: XSS - Location-based XSS
function redirectToProfile(userId) {
    // VULNERABLE: User input in location
    window.location.href = `/profile?id=${userId}`;
}

// VULNERABILITY: XSS - Event handler injection
function createButton(userInput) {
    const button = document.createElement('button');
    // VULNERABLE: User input in event handler
    button.onclick = function() { alert(userInput); };
    document.body.appendChild(button);
}

