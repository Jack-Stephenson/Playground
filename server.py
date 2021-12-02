from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def main_page():
    return render_template('index.html', numb=3)
@app.route('/play/<number>')
def count(number):
    return render_template('index.html', numb=int(number))
@app.route('/play/<number>/<colorr>')
def colorr(number, colorr):
    return render_template('index.html', numb=int(number), colorr=str(colorr))
if __name__=="__main__":
    app.run(debug=True)