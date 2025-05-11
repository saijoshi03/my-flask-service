===
📘 XSS DEMO WEBSITE 
===

📝 Description:
---------------
This is a simple demo website using only HTML and CSS that shows how a Cross-Site Scripting (XSS) vulnerability works. It is meant for educational purposes to learn about web security.

⚠️ WARNING: This website is intentionally insecure. Do not use this code in real-world websites.


🌐 LIVE DEMO LINK:
--------------------
https://my-flask-service-sj38.onrender.com


❓ WHAT IS XSS?
----------------
XSS stands for Cross-Site Scripting.

It is a type of attack where someone puts malicious code (usually JavaScript) into a website that is then shown to other users. This happens when a site does NOT clean or escape user input.

🧪 Try this example:

Type this into the input box on the page:
<script>alert('This is an XSS attack!')</script>

If you see a popup message, it means the website is vulnerable to XSS.


⚠️ WHY IS XSS DANGEROUS?
-------------------------
- Steal passwords or session tokens
- Redirect users to fake websites
- Modify the content of the website
- Show fake login forms
- Spread worms through links

These attacks can cause serious damage, especially on login pages or admin panels.


🛡️ HOW TO PREVENT XSS (Mitigation Tips)
----------------------------------------
✅ 1. Escape HTML characters like < > " ' in user input before showing it
✅ 2. Use frameworks (like React, Flask templates, etc.) that escape content by default
✅ 3. Use input sanitization libraries like DOMPurify
✅ 4. Add a Content Security Policy (CSP) header
✅ 5. Never insert raw user input into HTML, JavaScript, or URLs

Always treat user input as dangerous until you clean or escape it!


📁 PROJECT FILE STRUCTURE
--------------------------
index.html       → The main HTML file with the XSS form
style.css        → CSS file for page styling (optional)
README.txt       → This file


🎯 PURPOSE OF THIS DEMO
------------------------
This project is made to help students and beginners understand:

- How an XSS attack works
- Why input validation and escaping output are important
- How to test and prevent these security risks


📚 LEARN MORE
--------------
OWASP XSS Guide: https://owasp.org/www-community/attacks/xss  
GitHub Pages Help: https://pages.github.com/  
DOMPurify Library: https://github.com/cure53/DOMPurify  

===
Made for Learning Only ✨
===
