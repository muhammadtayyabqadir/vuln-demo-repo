"""
Database Utilities with SQL Injection Vulnerabilities
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

import sqlite3
import mysql.connector

# VULNERABILITY: SQL Injection - String formatting
def get_user_by_email(email):
    """Get user by email - VULNERABLE to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Using % formatting
    query = "SELECT * FROM users WHERE email = '%s'" % email
    cursor.execute(query)
    return cursor.fetchone()

# VULNERABILITY: SQL Injection - .format() method
def search_products(keyword):
    """Search products - VULNERABLE to SQL injection"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Using .format()
    query = "SELECT * FROM products WHERE name LIKE '%{}%'".format(keyword)
    cursor.execute(query)
    return cursor.fetchall()

# VULNERABILITY: SQL Injection - Multiple queries
def update_user_status(user_id, status):
    """Update user status - VULNERABLE to SQL injection"""
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
        database="mydb"
    )
    cursor = conn.cursor()
    
    # VULNERABLE: Multiple injection points
    query = f"UPDATE users SET status = '{status}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()
    conn.close()

# VULNERABILITY: SQL Injection - UNION-based
def get_user_data(user_id):
    """Get user data - VULNERABLE to UNION-based SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: UNION-based injection possible
    query = f"SELECT username, email FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()

# VULNERABILITY: SQL Injection - Time-based blind
def check_user_exists(username):
    """Check if user exists - VULNERABLE to time-based blind SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Time-based injection possible
    query = f"SELECT COUNT(*) FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] > 0

# VULNERABILITY: SQL Injection - Boolean-based blind
def authenticate(username, password):
    """Authenticate user - VULNERABLE to boolean-based blind SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Boolean-based injection possible
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return user is not None

