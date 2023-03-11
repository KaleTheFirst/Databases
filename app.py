from flask import Flask, render_template, request, redirect, url_for
import sqlite3







app = Flask(__name__)

@app.route('/')
def index():
    #trains = get_all_trains()

    return render_template('index.html')



# @app.route('/alter/<rowid>')
# def edit(rowid):
#     train = get_train(rowid)
#     return render_template('alter.html', train = train)




if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')

