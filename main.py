from flask import Flask, render_template, json, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_percent', methods=['GET', 'POST'])
def get_percent():
    print(request.form)
    my_summ = request.form['my_summ'];
    print(my_summ)
    if(my_summ.isdigit()):
        my_summ=int(my_summ)
        bank = int((my_summ/100)*20)
        myMoney = my_summ - bank
        return json.dumps({'percent': bank, 'myMoney': myMoney})
    else: return (json.dumps({'percent': 'Только цифры!', 'myMoney': ''}))

if __name__ == '__main__':
    app.run(debug=True)