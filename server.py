from flask import Flask, render_template, redirect,flash, request
from helpers import save_data_to_csv

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def welcome_msg():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    request_url = f'./{page_name}.html'
    return render_template(request_url)


@app.route('/submit_form',methods=['GET','POST'])
def submit_form():
    try:
        data = [*request.form].to_dict()
        save_data_to_csv(data)
        flash('Request has been submitted. I will get in touch with you shortly. Thank You!')
    except Exception as e:
      print(f'An exception occurred: {e}')
      flash("Something Wrong submitting the form. Try again later please.")
    return redirect('./index')
 

