import os
import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

#Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='',
    USERNAME='admin',
    PASSWORD='default',
    GOOGLE_SHEET_KEY='',
    JSON_KEYFILE_NAME='',
    GTPATH='FILL/hopper/grievances_to_air.txt',
    ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def get_worksheet():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(app.config['JSON_KEYFILE_NAME'],scope);
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_key(app.config['GOOGLE_SHEET_KEY'])
    worksheet = sheet.get_worksheet(0)
    return worksheet


@app.route('/')
def show_entries():
    worksheet = get_worksheet()
    rows =  worksheet.get_all_values()
    return render_template('show_entries.html', rows=rows)

@app.route('/ignore', methods=['GET'])
def ignore_entry():
    if not session.get('logged_in'):
        abort(401)
    if not request.args.get('row'):
        flash('No entry specified')
        return redirect(url_for('show_entries'))
    row = request.args.get('row')
    worksheet = get_worksheet()
    worksheet.update_cell(row,3, 'I')
    flash('Entry was ignored.')
    return redirect(url_for('show_entries'))


@app.route('/approve', methods=['GET'])
def approve_entry():
    if not session.get('logged_in'):
        abort(401)
    if not request.args.get('row'):
        flash('No entry specified')
        return redirect(url_for('show_entries'))
    
    row = request.args.get('row')
    worksheet = get_worksheet()
    cell = worksheet.cell(row,2)
    with open(app.config['GTPATH'], "a") as appFile:
        appFile.write(cell.value + "\n")

    worksheet.update_cell(row,3, 'A')

    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username or password'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

