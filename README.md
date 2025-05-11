#  XSS Demo Website (Static HTML + CSS)

This is a simple website made with only **HTML and CSS** to demonstrate a basic **Cross-Site Scripting (XSS)** vulnerability. It's intentionally insecure and meant only for learning how XSS works.

> **Warning:** This is for educational use only. Do not use insecure code like this in real applications.

---

## Live Demo

You can try the demo online here:  
https://my-flask-service-sj38.onrender.com

## ❓ What is XSS?

**Cross-Site Scripting (XSS)** is a type of web security issue where attackers inject malicious code (usually JavaScript) into websites viewed by other users.

### Example:
If you type this into a form:
```html
<script>alert('XSS')</script>

****Why XSS is Dangerous****
##An attacker can:##

    Show fake login forms to steal passwords

    Steal your session cookies and impersonate you

    Redirect you to malicious websites

    Modify the page content for phishing
