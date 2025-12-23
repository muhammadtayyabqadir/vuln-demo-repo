/**
 * Profile Page with General Security Vulnerabilities
 * WARNING: This code contains intentional vulnerabilities for testing purposes
 */

// VULNERABILITY: Missing HTTPS enforcement
function sendUserData(data) {
    // VULNERABLE: HTTP instead of HTTPS
    fetch('http://api.example.com/user', {
        method: 'POST',
        body: JSON.stringify(data)
    });
}

// VULNERABILITY: Insecure cookie settings
function setAuthCookie(token) {
    // VULNERABLE: Missing secure and httpOnly flags
    document.cookie = `auth_token=${token}; path=/`;
}

// VULNERABILITY: Weak password validation
function validatePassword(password) {
    // VULNERABLE: Too weak requirements
    if (password.length < 3) {
        return false;
    }
    return true;
}

// VULNERABILITY: Missing CSRF protection
function transferFunds(amount, recipient) {
    // VULNERABLE: No CSRF token
    fetch('/api/transfer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            amount: amount,
            recipient: recipient
        })
    });
}

// VULNERABILITY: Insecure storage of sensitive data
function saveCredentials(username, password) {
    // VULNERABLE: Storing password in localStorage
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);
}

// VULNERABILITY: Missing input validation
function processPayment(cardNumber, cvv) {
    // VULNERABLE: No validation on card number or CVV
    fetch('/api/payment', {
        method: 'POST',
        body: JSON.stringify({
            card: cardNumber,
            cvv: cvv
        })
    });
}

// VULNERABILITY: Information disclosure
function handleError(error) {
    // VULNERABLE: Exposing internal error details
    console.error('Database error:', error.stack);
    alert('Error: ' + error.message);
}

// VULNERABILITY: Missing authentication check
function deleteUser(userId) {
    // VULNERABLE: No authentication/authorization check
    fetch(`/api/users/${userId}`, {
        method: 'DELETE'
    });
}

