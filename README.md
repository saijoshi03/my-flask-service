==============================
📘 XSS DEMO WEBSITE
==============================

Hey there! 👋

This is a simple demo project where I’ve intentionally created a **Cross-Site Scripting (XSS)** vulnerability to help you understand how XSS attacks work. This is a **learning tool**, so you can test it out and see exactly what happens when user input isn’t sanitized properly. Don't worry, this site is insecure by design, and is not meant for use in real-world applications.

---

### 🚀 Live Demo

Check out the demo in action:  
🔗 **[Live Demo Here](https://your-username.github.io/your-repo-name/)**  
(Just replace "your-username" and "your-repo-name" with your GitHub username and repository name)

---

### ❓ What is XSS?

**Cross-Site Scripting (XSS)** is one of the most common web security vulnerabilities. It occurs when attackers inject malicious JavaScript code into websites. The malicious code is then executed in a user's browser when they visit the site.

In this demo, I’ve created a simple form that doesn’t clean or escape your input. So, when you type something like:

```html
<script>alert('XSS Attack!');</script>
