from flask import Flask,render_template
app=Flask(__name__)

@app.route('/<int:mark>')
def res(mark):
    return render_template('hello.html', marks =mark)

if __name__ == '__main__':
    app.run(debug=True)