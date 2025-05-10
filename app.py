from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        try:
            # Get the values from the form inputs
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            
            # Calculate the result
            result = a + b
            return render_template('index.html', result=f"The sum of {a} and {b} is {result}")
        except ValueError:
            return render_template('index.html', error="Invalid input. Please provide valid numeric values for 'a' and 'b'.")
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
