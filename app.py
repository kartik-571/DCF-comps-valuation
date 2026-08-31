from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        revenue = request.form["revenue"]
        return f"You entered: {revenue}"
    return '''
        <form method="POST">
            Revenue: <input type="text" name="revenue">
            <input type="submit">
            </form>
            '''

if __name__ == '__main__':
    app.run(debug=True)
