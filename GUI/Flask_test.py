from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('option.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['P_XS']
    processed_text = text.upper()
    print(processed_text)
    return processed_text

if __name__ == "__main__":
    app.run(debug=True)