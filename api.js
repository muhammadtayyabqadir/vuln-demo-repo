/**
 * API Client with Security Vulnerabilities
 * WARNING: This code contains intentional vulnerabilities for testing purposes
 */

// VULNERABILITY: Hardcoded API key in frontend
const API_KEY = "sk_live_51Hqj8K2J3mN4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM";

// VULNERABILITY: Insecure API endpoint
const API_BASE_URL = "http://api.example.com"; // Should be HTTPS

// VULNERABILITY: Missing authentication
function fetchUserData(userId) {
    // VULNERABLE: No authentication headers
    return fetch(`${API_BASE_URL}/users/${userId}`)
        .then(response => response.json());
}

// VULNERABILITY: Exposed sensitive data in requests
function updateProfile(userData) {
    // VULNERABLE: Sending password in plain text
    return fetch(`${API_BASE_URL}/profile`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-API-Key': API_KEY // VULNERABLE: API key in headers
        },
        body: JSON.stringify({
            username: userData.username,
            password: userData.password, // Should never be sent
            email: userData.email
        })
    });
}

// VULNERABILITY: Missing rate limiting on client side
function sendMessage(message) {
    // VULNERABLE: No rate limiting
    for (let i = 0; i < 1000; i++) {
        fetch(`${API_BASE_URL}/messages`, {
            method: 'POST',
            body: JSON.stringify({ message: message })
        });
    }
}

// VULNERABILITY: Insecure data transmission
function uploadFile(file) {
    // VULNERABLE: No encryption, plain HTTP
    const formData = new FormData();
    formData.append('file', file);
    
    return fetch('http://upload.example.com/upload', {
        method: 'POST',
        body: formData
    });
}

