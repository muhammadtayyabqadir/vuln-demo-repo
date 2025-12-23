"""
Backend API with SQL Injection Vulnerabilities
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# VULNERABILITY: SQL Injection - Direct string concatenation
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID - VULNERABLE to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string interpolation
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    return jsonify(user)

# VULNERABILITY: SQL Injection - Unsanitized input
@app.route('/search', methods=['POST'])
def search_users():
    """Search users - VULNERABLE to SQL injection"""
    data = request.get_json()
    search_term = data.get('search', '')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: String concatenation in SQL
    query = "SELECT * FROM users WHERE name LIKE '%" + search_term + "%'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return jsonify(results)

# VULNERABILITY: SQL Injection - Multiple injection points
@app.route('/filter', methods=['GET'])
def filter_users():
    """Filter users - VULNERABLE to SQL injection"""
    username = request.args.get('username', '')
    email = request.args.get('email', '')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Multiple unsanitized inputs
    query = f"SELECT * FROM users WHERE username = '{username}' AND email = '{email}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return jsonify(results)

# VULNERABILITY: SQL Injection - Raw SQL execution
@app.route('/admin/users', methods=['GET'])
def admin_get_users():
    """Admin endpoint - VULNERABLE to SQL injection"""
    role = request.args.get('role', 'user')
    status = request.args.get('status', 'active')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Building query with user input
    query = f"SELECT * FROM users WHERE role = '{role}' AND status = '{status}'"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

