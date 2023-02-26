from flask import Flask, render_template
app=Flask(__name__)

@app.route('/result/10')
def result():
    dict = {'math':70, 'phy':80, 'eng':100}
    return render_template('result.html', result = dict)

if __name__=='__main__':
    app.run(debug=True)