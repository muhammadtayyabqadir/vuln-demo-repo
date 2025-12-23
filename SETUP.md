# Setup Instructions for Vulnerability Demo Repository

## Quick Start

This repository is ready to be uploaded to GitHub and used with Catch & Patch security scanner.

## Steps to Upload to GitHub

1. **Initialize Git Repository** (if not already done):
   ```bash
   cd vuln-demo-repo
   git init
   git add .
   git commit -m "Initial commit: Vulnerability demo repository"
   ```

2. **Create GitHub Repository**:
   - Go to GitHub.com
   - Click "New repository"
   - Name it: `vuln-demo-repo` (or any name you prefer)
   - Make it **public** (so Catch & Patch can access it)
   - Don't initialize with README (we already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/vuln-demo-repo.git
   git branch -M main
   git push -u origin main
   ```

## Using with Catch & Patch

1. **Start Catch & Patch**:
   - Follow the setup instructions in the main Catch & Patch repository
   - Ensure both backend and frontend are running

2. **Access the Dashboard**:
   - Navigate to `http://localhost:3000`

3. **Start a Scan**:
   - Enter your repository URL: `https://github.com/YOUR_USERNAME/vuln-demo-repo`
   - Click "Start Scan"
   - Wait for all scanners to complete

4. **Review Results**:
   - View the security report
   - Check detected vulnerabilities
   - Review generated patches
   - Test red team scenarios

## Expected Vulnerabilities

This repository should trigger detections for:

- **SQL Injection**: Multiple instances in `backend/api.py` and `utils/database.py`
- **XSS**: Multiple instances in `backend/user_controller.py` and `frontend/login.js`
- **Secret Leaks**: Multiple API keys, passwords, and tokens in `backend/config.py` and `frontend/api.js`
- **General Security Issues**: Weak validation, missing HTTPS, insecure storage in `backend/auth.py` and `frontend/profile.js`
- **AI/LLM Vulnerabilities**: Prompt injection, data exposure in `ai/chatbot.py`

## Testing Different Scanners

Each scanner should detect specific vulnerabilities:

- **SQL Injection Scanner**: Should find 8+ SQL injection vulnerabilities
- **XSS Scanner**: Should find 10+ XSS vulnerabilities
- **Secret Leak Scanner**: Should find 15+ secret leaks
- **General Scanner**: Should find 10+ general security issues
- **AI Scanner**: Should find 5+ AI/LLM-related vulnerabilities

## Notes

- All vulnerabilities are **intentional** for testing purposes
- **DO NOT** use this code in production
- This repository is for educational and testing purposes only
- Feel free to modify or add more vulnerabilities for testing

## Troubleshooting

If scanners don't detect vulnerabilities:
- Ensure the repository is public on GitHub
- Check that the repository URL is correct
- Verify all scanners are running properly
- Check backend logs for any errors

