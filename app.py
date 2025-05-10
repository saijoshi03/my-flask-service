from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/add')
def add_numbers():
    try:
        # Get the 'a' and 'b' query parameters, defaulting to 0 if not provided
        a = request.args.get('a', type=float, default=0)
        b = request.args.get('b', type=float, default=0)

        # Check if the inputs are valid numbers
        if a is None or b is None:
            return "Invalid input. Please provide valid numeric values for 'a' and 'b'.", 400
        
        result = a + b
        return f"The sum of {a} and {b} is {result}"
    except ValueError:
        return "Invalid input. Please provide numeric values for 'a' and 'b'.", 400

if __name__ == '__main__':
    # Get the port from the environment variable for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
