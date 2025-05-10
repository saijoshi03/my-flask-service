from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/add')
def add_numbers():
    try:
        # Get query parameters
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return f"The sum of {a} and {b} is {result}"
    except ValueError:
        return "Invalid input. Please provide numeric values for a and b."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
