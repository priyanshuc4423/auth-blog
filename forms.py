from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL,email_validator,Length,Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterUser(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired()])
    email = StringField(label="EMAIL",validators=[DataRequired()])
    password = PasswordField(label='PASSWORD',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField("SUBMIT")


class Login(FlaskForm):
    email = StringField(label='email',validators=[DataRequired(),Email(message='Please enter a valid mail')])
    password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='submit')

class Commentform(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField(label='Submit Comment')