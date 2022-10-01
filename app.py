from crypt import methods
from decimal import Decimal
from unittest import result
from flask import Flask, request, render_template, jsonify, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

app = Flask(__name__)
app.config['SECRET_KEY'] = "qwerty123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/bitcoin')
def bitcoin_page():
    return render_template("bitcoin.html")

@app.route('/symbol')
def symbol_page():
    return render_template("symbol.html")

@app.route('/currency-rate', methods = ['POST'])
def converter():
    cur1 = request.form["cur1"]
    cur2 = request.form["cur2"]
    amount = request.form["amount"]
    total = cur1 + cur2
    c = CurrencyRates()
    result = c.convert(cur1, cur2, float(amount))

    return render_template('home.html', total=total, result=result)

@app.route('/bitcoin-price', methods=['POST'])
def bitcoin():
    cur = request.form["cur"].upper()
    b = BtcConverter()
    s = CurrencyCodes()
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    result = "The price of bitcoin as of " + str(now) + " is " + s.get_symbol(cur) + str(round(b.get_latest_price(cur), 2))

    return render_template("bitcoin.html", result = result)

@app.route('/currency-symbol', methods=['POST'])
def symbol():
    cur = request.form["cur"].upper()
    s = CurrencyCodes()
    result = s.get_symbol(cur)

    return render_template("symbol.html", result = result)
