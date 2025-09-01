### **Flask-JWT: A Brief Explanation**

**Flask-JWT** (or more commonly, **Flask-JWT-Extended**) is an **extension for Flask** that provides **JSON Web Token (JWT) authentication** for securing APIs. JWTs are a **stateless, compact, and URL-safe** way to authenticate users and transmit information between parties as a JSON object. Flask-JWT-Extended simplifies the process of **generating, validating, and managing JWTs** in Flask applications.

---

- [**1. What is JWT?**](#1-what-is-jwt)
- [**2. Why Use Flask-JWT-Extended?**](#2-why-use-flask-jwt-extended)
- [**3. Key Features of Flask-JWT-Extended**](#3-key-features-of-flask-jwt-extended)
  - [**3.1. Token Creation and Validation**](#31-token-creation-and-validation)
  - [**3.2. Protected Routes**](#32-protected-routes)
  - [**3.3. Custom Claims**](#33-custom-claims)
  - [**3.4. Refresh Tokens**](#34-refresh-tokens)
  - [**3.5. Token Blacklisting**](#35-token-blacklisting)
  - [**3.6. Token in Headers**](#36-token-in-headers)
- [**4. Installation**](#4-installation)
- [**5. Basic Setup**](#5-basic-setup)
  - [**5.1. Configure Flask-JWT-Extended**](#51-configure-flask-jwt-extended)
  - [**5.2. Create Login and Protected Routes**](#52-create-login-and-protected-routes)
  - [**5.3. Run the App**](#53-run-the-app)
  - [**5.4. Test the API**](#54-test-the-api)
- [**6. Advanced Features**](#6-advanced-features)
  - [**6.1. Custom JWT Callbacks**](#61-custom-jwt-callbacks)
  - [**6.2. Token Freshness**](#62-token-freshness)
  - [**6.3. Token in Cookies**](#63-token-in-cookies)
  - [**6.4. Revoking Tokens**](#64-revoking-tokens)
- [**7. Flask-JWT-Extended vs. Flask-JWT**](#7-flask-jwt-extended-vs-flask-jwt)
- [**8. Strengths of Flask-JWT-Extended**](#8-strengths-of-flask-jwt-extended)
- [**9. Weaknesses of Flask-JWT-Extended**](#9-weaknesses-of-flask-jwt-extended)
- [**10. When to Use Flask-JWT-Extended**](#10-when-to-use-flask-jwt-extended)
- [**11. Example: Full Authentication Flow**](#11-example-full-authentication-flow)
  - [**11.1. User Model and Database Setup**](#111-user-model-and-database-setup)
  - [**11.2. Register and Login Routes**](#112-register-and-login-routes)
  - [**11.3. Refresh Token Route**](#113-refresh-token-route)
  - [**11.4. Protected Route with Role Check**](#114-protected-route-with-role-check)
- [**12. Learning Resources**](#12-learning-resources)
- [**13. Summary**](#13-summary)


## **1. What is JWT?**
**JSON Web Token (JWT)** is a **standard (RFC 7519)** for securely transmitting information between parties as a JSON object. It consists of three parts:
1. **Header**: Contains metadata (e.g., token type, algorithm).
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```
2. **Payload**: Contains claims (e.g., user ID, expiration time).
   ```json
   {
     "sub": "1234567890",
     "name": "Alice",
     "iat": 1516239022
   }
   ```
3. **Signature**: Ensures the token hasn’t been tampered with (generated using a secret key).

**Example JWT**:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsaWNlIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

---

## **2. Why Use Flask-JWT-Extended?**
- **Stateless Authentication**: No server-side session storage required.
- **Secure**: Tokens are signed and can be verified.
- **Flexible**: Supports custom claims and token expiration.
- **Easy Integration**: Works seamlessly with Flask routes.
- **Extensible**: Supports refresh tokens, blacklisting, and more.

---

## **3. Key Features of Flask-JWT-Extended**

### **3.1. Token Creation and Validation**
- **Generate Tokens**: Create access and refresh tokens.
- **Validate Tokens**: Automatically verify tokens in protected routes.

---

### **3.2. Protected Routes**
- Use decorators to **restrict access** to authenticated users.
  ```python
  from flask_jwt_extended import jwt_required

  @app.route('/protected', methods=['GET'])
  @jwt_required()
  def protected():
      return {"message": "This is a protected route!"}
  ```

---

### **3.3. Custom Claims**
- Add **custom data** to JWT payloads.
  ```python
  from flask_jwt_extended import create_access_token

  access_token = create_access_token(identity=user_id, additional_claims={"role": "admin"})
  ```

---

### **3.4. Refresh Tokens**
- Issue **short-lived access tokens** and **long-lived refresh tokens** for improved security.
  ```python
  from flask_jwt_extended import create_refresh_token

  refresh_token = create_refresh_token(identity=user_id)
  ```

---

### **3.5. Token Blacklisting**
- **Revoke tokens** before they expire (e.g., on logout).
  ```python
  from flask_jwt_extended import get_jti
  from flask_jwt_extended.token_store import TokenStore

  @app.route('/logout', methods=['DELETE'])
  @jwt_required()
  def logout():
      jti = get_jti(current_token)
      token_store = TokenStore()
      token_store.add(jti)  # Blacklist the token
      return {"message": "Successfully logged out"}
  ```

---

### **3.6. Token in Headers**
- Tokens are typically sent in the **Authorization header**:
  ```
  Authorization: Bearer <your_token_here>
  ```

---

## **4. Installation**

```bash
pip install flask-jwt-extended
```

---

## **5. Basic Setup**

### **5.1. Configure Flask-JWT-Extended**
```python
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configure JWT
app.config["JWT_SECRET_KEY"] = "your-secret-key"  # Change this!
jwt = JWTManager(app)
```

---

### **5.2. Create Login and Protected Routes**
```python
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Mock user database
users = {
    "alice": {"password": "secret", "role": "admin"},
    "bob": {"password": "password", "role": "user"}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or user["password"] != password:
        return jsonify({"msg": "Bad username or password"}), 401

    # Create access token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
```

---

### **5.3. Run the App**
```bash
flask run
```

---

### **5.4. Test the API**
- **Login**:
  ```bash
  curl -X POST http://127.0.0.1:5000/login \
       -H "Content-Type: application/json" \
       -d '{"username": "alice", "password": "secret"}'
  ```
  **Response**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
  ```

- **Access Protected Route**:
  ```bash
  curl http://127.0.0.1:5000/protected \
       -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  ```
  **Response**:
  ```json
  {
    "logged_in_as": "alice"
  }
  ```

---

## **6. Advanced Features**

### **6.1. Custom JWT Callbacks**
- **Modify Token Creation/Validation**:
  ```python
  @jwt.token_in_blocklist_loader
  def check_if_token_revoked(jwt_header, jwt_payload):
      jti = jwt_payload["jti"]
      return jti in token_blocklist  # Check if token is blacklisted

  @jwt.user_identity_loader
  def user_identity_lookup(user):
      return user.id  # Use user ID as identity
  ```

---

### **6.2. Token Freshness**
- **Require Fresh Tokens** for sensitive operations:
  ```python
  @app.route('/admin', methods=['GET'])
  @jwt_required(fresh=True)
  def admin():
      return jsonify({"message": "Admin access granted"})
  ```

---

### **6.3. Token in Cookies**
- **Store Tokens in HTTP-Only Cookies** for security:
  ```python
  app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
  app.config["JWT_COOKIE_SECURE"] = True  # HTTPS only
  app.config["JWT_COOKIE_CSRF_PROTECT"] = True  # Enable CSRF protection
  ```

---

### **6.4. Revoking Tokens**
- **Blacklist Tokens** on logout:
  ```python
  from flask_jwt_extended import get_jti

  token_blocklist = set()

  @app.route('/logout', methods=['DELETE'])
  @jwt_required()
  def logout():
      jti = get_jti(current_token)
      token_blocklist.add(jti)
      return jsonify({"message": "Successfully logged out"})
  ```

---

## **7. Flask-JWT-Extended vs. Flask-JWT**

| **Feature**               | **Flask-JWT-Extended**                     | **Flask-JWT (Deprecated)**               |
|---------------------------|---------------------------------------------|------------------------------------------|
| **Maintenance**           | Actively maintained                        | Deprecated (use Flask-JWT-Extended)      |
| **Refresh Tokens**        | ✅ Built-in support                        | ❌ No built-in support                  |
| **Token Blacklisting**    | ✅ Easy to implement                       | ❌ Limited support                      |
| **Custom Claims**         | ✅ Full support                           | ❌ Limited support                      |
| **CSRF Protection**       | ✅ Built-in                               | ❌ No built-in support                  |
| **Documentation**         | ✅ Comprehensive                           | ❌ Outdated                             |

---

## **8. Strengths of Flask-JWT-Extended**

✅ **Easy to Use**: Simple setup and integration with Flask.
✅ **Stateless**: No server-side session storage required.
✅ **Secure**: Supports token signing, expiration, and blacklisting.
✅ **Flexible**: Customize token creation, validation, and claims.
✅ **Refresh Tokens**: Issue short-lived access tokens and long-lived refresh tokens.
✅ **Extensible**: Add custom logic for token handling.

---

## **9. Weaknesses of Flask-JWT-Extended**

❌ **Token Storage**: Requires a **database or cache** (e.g., Redis) for blacklisting tokens.
❌ **Complexity**: Managing token expiration and refresh logic can be tricky.
❌ **Performance**: Token validation adds overhead to each request.

---

## **10. When to Use Flask-JWT-Extended**

- **API Authentication**: Secure REST APIs with JWT.
- **Stateless Apps**: When you don’t want to manage server-side sessions.
- **Microservices**: Authenticate requests between services.
- **Single-Page Applications (SPAs)**: Frontend apps (React, Vue) can store tokens and make authenticated requests.

---

## **11. Example: Full Authentication Flow**

### **11.1. User Model and Database Setup**
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()
```

---

### **11.2. Register and Login Routes**
```python
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200
```

---

### **11.3. Refresh Token Route**
```python
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_token), 200
```

---

### **11.4. Protected Route with Role Check**
```python
@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user.username != "admin":
        return jsonify({"msg": "Admin access required"}), 403

    return jsonify({"message": "Welcome, admin!"}), 200
```

---

## **12. Learning Resources**

- **Official Documentation**: [flask-jwt-extended.readthedocs.io](https://flask-jwt-extended.readthedocs.io/)
- **Tutorials**:
  - [Flask-JWT-Extended Tutorial (Real Python)](https://realpython.com/token-based-authentication-with-flask/)
  - [Flask-JWT-Extended Example (TestDriven.io)](https://testdriven.io/blog/flask-jwt-auth/)
- **GitHub**: [vimalloc/flask-jwt-extended](https://github.com/vimalloc/flask-jwt-extended)

---

## **13. Summary**

- **Flask-JWT-Extended** is a **powerful, flexible extension** for adding **JWT authentication** to Flask applications.
- **Key Features**: Token creation/validation, protected routes, refresh tokens, and custom claims.
- **Strengths**: Stateless, secure, and easy to integrate with Flask.
- **Weaknesses**: Requires token storage for blacklisting and can add complexity.
- **Use Cases**: Ideal for **securing APIs, microservices, and SPAs** where stateless authentication is desired.

Flask-JWT-Extended is the **go-to choice** for Flask developers who need a **robust, modern authentication system** without the overhead of session management.