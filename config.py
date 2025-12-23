"""
Configuration File with Secret Leaks
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

# VULNERABILITY: Hardcoded API keys
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILITY: Database credentials in source code
DATABASE_URL = "postgresql://admin:SuperSecretPassword123@localhost:5432/mydb"
DATABASE_USER = "admin"
DATABASE_PASSWORD = "SuperSecretPassword123"

# VULNERABILITY: API keys exposed
STRIPE_API_KEY = "sk_live_51Hqj8K2J3mN4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM"
STRIPE_SECRET_KEY = "sk_live_51Hqj8K2J3mN4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM"

# VULNERABILITY: GitHub token
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

# VULNERABILITY: JWT secret
JWT_SECRET = "my-super-secret-jwt-key-that-should-not-be-here"

# VULNERABILITY: OAuth credentials
GOOGLE_CLIENT_ID = "123456789-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "GOCSPX-abcdefghijklmnopqrstuvwxyz"

# VULNERABILITY: MongoDB connection string with credentials
MONGODB_URI = "mongodb://admin:password123@cluster0.mongodb.net:27017/mydb"

# VULNERABILITY: Redis password
REDIS_PASSWORD = "redis_password_12345"

# VULNERABILITY: Slack webhook URL (contains token)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# VULNERABILITY: Email credentials
SMTP_USERNAME = "admin@example.com"
SMTP_PASSWORD = "EmailPassword123!"

# VULNERABILITY: Encryption key
ENCRYPTION_KEY = "0123456789abcdef0123456789abcdef"

