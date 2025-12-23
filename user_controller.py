"""
User Controller with XSS Vulnerabilities
WARNING: This code contains intentional vulnerabilities for testing purposes
"""

from flask import Flask, request, jsonify, render_template_string
import html

app = Flask(__name__)

# VULNERABILITY: XSS - Direct output without escaping
@app.route('/profile/<username>')
def user_profile(username):
    """User profile page - VULNERABLE to XSS"""
    # VULNERABLE: Direct template rendering without escaping
    template = f"""
    <html>
    <body>
        <h1>Welcome, {username}!</h1>
        <p>Your profile information</p>
    </body>
    </html>
    """
    return render_template_string(template)

# VULNERABILITY: XSS - Unsanitized user input in HTML
@app.route('/comment', methods=['POST'])
def add_comment():
    """Add comment - VULNERABLE to XSS"""
    data = request.get_json()
    comment = data.get('comment', '')
    user = data.get('user', '')
    
    # VULNERABLE: Direct HTML injection
    html_response = f"""
    <div class="comment">
        <strong>{user}</strong> said: {comment}
    </div>
    """
    return html_response

# VULNERABILITY: XSS - Reflected XSS in search
@app.route('/search')
def search():
    """Search page - VULNERABLE to reflected XSS"""
    query = request.args.get('q', '')
    
    # VULNERABLE: No output encoding
    return f"""
    <html>
    <body>
        <h1>Search Results</h1>
        <p>You searched for: {query}</p>
    </body>
    </html>
    """

# VULNERABILITY: XSS - Stored XSS
comments = []

@app.route('/forum/post', methods=['POST'])
def post_message():
    """Post forum message - VULNERABLE to stored XSS"""
    data = request.get_json()
    message = data.get('message', '')
    author = data.get('author', '')
    
    # VULNERABLE: Storing unsanitized HTML
    comments.append({
        'author': author,
        'message': message,
        'timestamp': '2024-01-01'
    })
    
    return jsonify({'status': 'success'})

@app.route('/forum')
def forum():
    """Forum page - VULNERABLE to stored XSS"""
    # VULNERABLE: Rendering stored unsanitized content
    html_content = "<h1>Forum Posts</h1>"
    for comment in comments:
        html_content += f"""
        <div class="post">
            <strong>{comment['author']}</strong>: {comment['message']}
        </div>
        """
    return html_content

# VULNERABILITY: XSS - DOM-based XSS
@app.route('/api/user-data')
def get_user_data():
    """Get user data - VULNERABLE to DOM-based XSS"""
    user_id = request.args.get('id', '')
    # VULNERABLE: Returning data that will be used in JavaScript
    return jsonify({
        'id': user_id,
        'name': request.args.get('name', ''),
        'email': request.args.get('email', '')
    })

