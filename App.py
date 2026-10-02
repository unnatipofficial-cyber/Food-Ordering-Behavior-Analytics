from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Renders the index.html file inside the templates folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)