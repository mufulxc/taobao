from flask import Flask, render_template
from db import fetch_sql
import os

app = Flask(__name__) 

@app.route('/')
def index():
    data = fetch_sql("SELECT * FROM taobao_stock_qty")
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
