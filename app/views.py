import os
from app import app
from flask import Flask, render_template, url_for, redirect, request, flash
from werkzeug.utils import secure_filename
from .utils import Calculations, allowed_file
from .forms import CalcData
import pandas as pd


@app.route('/', methods=['get', 'post'])
def index():
    form = CalcData()
    if form.validate_on_submit():
        if form.table.data:
            file = request.files['table']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                clients_table = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                newfunc = Calculations(clients_table)
                newfunc.squaretype(int(form.rtype.data))
                show_pic = True
                return render_template('main_page.html',
                                       form=form,
                                       list_of_c=newfunc.list_of_c,
                                       func=newfunc.func,
                                       show_pic=show_pic)
            else:
                flash('feed me an xlsx file, pls')
        else:
            flash('pls, feed me an xlsx file')
        # return redirect(url_for('index'))
    return render_template('main_page.html', form=form)
