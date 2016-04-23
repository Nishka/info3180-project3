"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,Flask,flash,jsonify
from flask.ext.wtf import Form
from wtforms import TextField, FileField,SelectField
from wtforms.validators import Required, Email

class ProfileForm(Form):  
    first_name = TextField('Firstname', validators = [Required()])
    last_name = TextField('Lastname', validators = [Required()])
    image = TextField('Image', validators = [Required(), Email()])

###
# Routing for your application.
###

@app.route('/signup/')
def home():
    """Render website's signup page."""
    return render_template("signup.html", error=error)

@app.route('/api/thumbnail/process', methods=['GET'])
def process_thumbnail():
    pass

@app.route('/api/user/register', methods =['GET', 'POST'])
def user_register():
    pass

@app.route('/api/user/login',methods = ['GET', 'POST'])
def user_login():
    pass

@app.route('/api/user/:id/wishlist', methods = ['GET','POST'])
def user_wishlist(id):
    pass


# @app.route('//')
# def profile_add(form=form):
#     form = ProfileForm()
#     return render_template('profile_add.html', form= form)
    
# @app.route('/profiles/')
# def profile_list():
#     return "list all profiles"    

# app.route('/profile/<int:id>/')
# def profile_view(id):
#     return "pofile()".format(id)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
  #  response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
