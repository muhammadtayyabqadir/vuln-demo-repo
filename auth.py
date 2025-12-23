"""
Authentication Module with Security Vulnerabilities
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

import hashlib
import random
import jwt
from datetime import datetime

# VULNERABILITY: Weak password hashing
def hash_password(password):
    """Hash password using MD5 - VULNERABLE (MD5 is broken)"""
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILITY: Insecure random number generation
def generate_session_token():
    """Generate session token - VULNERABLE (using random, not secrets)"""
    return str(random.randint(100000, 999999))

# VULNERABILITY: Hardcoded secret key
SECRET_KEY = "my-secret-key-12345"  # Should be in environment variable

def create_jwt_token(user_id, username):
    """Create JWT token - VULNERABLE (hardcoded secret)"""
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.utcnow().timestamp() + 3600
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# VULNERABILITY: Weak password validation
def validate_password(password):
    """Validate password - VULNERABLE (too weak requirements)"""
    if len(password) < 4:  # Too short
        return False
    return True

# VULNERABILITY: Missing rate limiting
def login(username, password):
    """Login function - VULNERABLE (no rate limiting)"""
    hashed = hash_password(password)
    # Check against database...
    return True

# VULNERABILITY: Insecure token storage
tokens = {}  # In-memory storage, no expiration

def store_token(user_id, token):
    """Store token - VULNERABLE (no expiration, in-memory)"""
    tokens[user_id] = token

