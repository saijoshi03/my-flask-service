# XSS DEMO WEBSITE

## Description
This is a simple demo website using only HTML and CSS that demonstrates how a Cross-Site Scripting (XSS) vulnerability works.  
It is meant for educational purposes to help learners understand basic web security risks.

> **WARNING:** This website is intentionally insecure. Do not use this code in real-world websites or production environments.

## Live Demo Link
[https://my-flask-service-sj38.onrender.com](https://my-flask-service-sj38.onrender.com)

## What is XSS?
XSS stands for **Cross-Site Scripting**.

It is a type of security vulnerability where attackers inject malicious code (usually JavaScript) into a website,  
which is then executed by unsuspecting users' browsers. This typically occurs when a site fails to properly sanitize user input.

### Example
Try typing the following into the input box on the website:

```html
<script>alert('This is an XSS attack!')</script>
```

If a popup appears, that means the site is vulnerable to an XSS attack.

These threats can lead to serious consequences, especially on sites with login pages, sensitive data, or admin access.

## Purpose of This Demo
This project is designed to help students and beginners understand:
- How XSS attacks work in web environments  
- The importance of validating and escaping user inputs  
- How to recognize and prevent these types of vulnerabilities  


