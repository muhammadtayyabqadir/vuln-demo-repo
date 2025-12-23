# Vulnerability Catalog

This document lists all intentional vulnerabilities in this demo repository for testing purposes.

## SQL Injection Vulnerabilities (8+ instances)

### Location: `backend/api.py`
1. **Line 12**: Direct string interpolation in SQL query (`get_user`)
2. **Line 25**: String concatenation in LIKE query (`search_users`)
3. **Line 38**: Multiple unsanitized inputs in WHERE clause (`filter_users`)
4. **Line 50**: Admin endpoint with SQL injection (`admin_get_users`)

### Location: `utils/database.py`
5. **Line 12**: % formatting in SQL query (`get_user_by_email`)
6. **Line 22**: .format() method in SQL query (`search_products`)
7. **Line 35**: Multiple injection points in UPDATE query (`update_user_status`)
8. **Line 47**: UNION-based SQL injection (`get_user_data`)
9. **Line 58**: Time-based blind SQL injection (`check_user_exists`)
10. **Line 70**: Boolean-based blind SQL injection (`authenticate`)

## XSS (Cross-Site Scripting) Vulnerabilities (10+ instances)

### Location: `backend/user_controller.py`
1. **Line 12**: Direct template rendering without escaping (`user_profile`)
2. **Line 25**: Direct HTML injection in comment (`add_comment`)
3. **Line 36**: Reflected XSS in search results (`search`)
4. **Line 50**: Stored XSS in forum posts (`post_message`, `forum`)
5. **Line 70**: DOM-based XSS in API response (`get_user_data`)

### Location: `frontend/login.js`
6. **Line 6**: Direct innerHTML assignment (`displayWelcomeMessage`)
7. **Line 14**: Direct HTML injection from URL params (`showError`)
8. **Line 21**: eval() with user input (`processUserInput`)
9. **Line 28**: document.write with user data (`renderUserProfile`)
10. **Line 36**: innerHTML with user-controlled data (`updateProfile`)
11. **Line 44**: Location-based XSS (`redirectToProfile`)
12. **Line 50**: Event handler injection (`createButton`)

## Secret Leak Vulnerabilities (15+ instances)

### Location: `backend/config.py`
1. **Line 5**: AWS Access Key ID
2. **Line 6**: AWS Secret Access Key
3. **Line 9**: Database URL with credentials
4. **Line 10**: Database username
5. **Line 11**: Database password
6. **Line 14**: Stripe API key
7. **Line 15**: Stripe secret key
8. **Line 18**: GitHub token
9. **Line 21**: JWT secret
10. **Line 24**: Google OAuth client ID
11. **Line 25**: Google OAuth client secret
12. **Line 28**: MongoDB connection string with credentials
13. **Line 31**: Redis password
14. **Line 34**: Slack webhook URL (contains token)
15. **Line 37**: SMTP username
16. **Line 38**: SMTP password
17. **Line 41**: Encryption key

### Location: `frontend/api.js`
18. **Line 4**: Hardcoded API key in frontend code
19. **Line 20**: API key in request headers

### Location: `ai/chatbot.py`
20. **Line 7**: OpenAI API key hardcoded

## General Security Vulnerabilities (10+ instances)

### Location: `backend/auth.py`
1. **Line 7**: Weak password hashing (MD5)
2. **Line 12**: Insecure random number generation
3. **Line 16**: Hardcoded secret key
4. **Line 20**: Weak password validation (minimum 4 characters)
5. **Line 26**: Missing rate limiting on login
6. **Line 30**: Insecure token storage (no expiration)

### Location: `frontend/profile.js`
7. **Line 4**: Missing HTTPS enforcement
8. **Line 10**: Insecure cookie settings (missing secure/httpOnly)
9. **Line 16**: Weak password validation
10. **Line 22**: Missing CSRF protection
11. **Line 28**: Insecure storage of sensitive data (localStorage)
12. **Line 34**: Missing input validation
13. **Line 40**: Information disclosure (error details)
14. **Line 46**: Missing authentication check

### Location: `frontend/api.js`
15. **Line 7**: Insecure API endpoint (HTTP)
16. **Line 13**: Missing authentication
17. **Line 20**: Exposed sensitive data in requests
18. **Line 32**: Missing rate limiting
19. **Line 38**: Insecure data transmission

## AI/LLM Vulnerabilities (5+ instances)

### Location: `ai/chatbot.py`
1. **Line 15**: Prompt injection - No input validation (`chat`)
2. **Line 30**: Prompt injection - System prompt manipulation (`assistant`)
3. **Line 45**: Training data exposure risk (`analyze_data`)
4. **Line 60**: No input length limits - Resource exhaustion (`summarize`)
5. **Line 75**: Unvalidated model outputs (`generate_content`)
6. **Line 90**: Insecure model configuration (`initialize_model`)

## Summary

- **Total SQL Injection**: 10 instances
- **Total XSS**: 12 instances
- **Total Secret Leaks**: 20 instances
- **Total General Security Issues**: 19 instances
- **Total AI/LLM Vulnerabilities**: 6 instances

**Grand Total: 67+ intentional vulnerabilities**

All vulnerabilities are clearly marked with `# VULNERABLE:` or `// VULNERABLE:` comments for easy identification.

