from flask_wtf import FlaskForm
from wtforms import StringField,ValidationError,TextAreaField,SubmitField,PasswordField,BooleanField,RadioField
from wtforms.validators import Required,Email,EqualTo

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What would you like to pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[Required()])
	submit = SubmitField('Submit')
class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')


class Downvote(FlaskForm):
	submit = SubmitField()