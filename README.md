# Vulnerability Demo Repository

This repository contains intentionally vulnerable code for testing security scanning tools, specifically **Catch & Patch**.

## ⚠️ WARNING

**This repository contains intentionally vulnerable code. DO NOT use this code in production!**

## Purpose

This demo repository is designed to test and demonstrate the capabilities of security scanning tools. It includes various types of vulnerabilities:

- SQL Injection vulnerabilities
- Cross-Site Scripting (XSS) vulnerabilities
- Secret leaks (API keys, passwords, tokens)
- General security issues
- AI/LLM-related vulnerabilities

## Repository Structure

```
vuln-demo-repo/
├── backend/
│   ├── api.py              # SQL injection vulnerabilities
│   ├── auth.py             # Authentication vulnerabilities
│   ├── config.py           # Secret leaks
│   └── user_controller.py  # XSS vulnerabilities
├── frontend/
│   ├── login.js            # XSS vulnerabilities
│   ├── profile.js          # General security issues
│   └── api.js              # Insecure API calls
├── ai/
│   └── chatbot.py          # AI/LLM vulnerabilities
└── utils/
    └── database.py         # SQL injection examples
```

## How to Use

1. Upload this repository to GitHub
2. Use the repository URL with Catch & Patch security scanner
3. Review the detected vulnerabilities and generated patches

## Vulnerability Types Included

### SQL Injection
- Direct string concatenation in SQL queries
- Unsanitized user input in database operations
- Raw SQL queries without parameterization

### XSS (Cross-Site Scripting)
- Unsanitized user input in HTML output
- Direct DOM manipulation with user data
- Missing output encoding

### Secret Leaks
- Hardcoded API keys
- Database credentials in source code
- JWT secrets and tokens
- AWS access keys

### General Security Issues
- Weak password validation
- Missing authentication checks
- Insecure random number generation
- Missing HTTPS enforcement

### AI/LLM Vulnerabilities
- Prompt injection vulnerabilities
- Unvalidated AI model inputs
- Training data exposure risks

## Testing with Catch & Patch

1. Clone or fork this repository
2. Navigate to your Catch & Patch instance
3. Enter the repository URL: `https://github.com/yourusername/vuln-demo-repo`
4. Start the scan
5. Review the generated security report
6. Examine the automated patches
7. Test the red team scenarios

## License

This repository is provided for educational and testing purposes only.

