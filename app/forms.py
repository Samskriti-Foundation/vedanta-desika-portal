from wtforms import Form, BooleanField, StringField, validators


class LoginForm(Form):
    email: StringField = StringField(
        "Email",
        [
            validators.DataRequired(),
            validators.Email(),
        ]
    )
    password: StringField = StringField(
        "Password",
        [
            validators.DataRequired(),
            validators.Length(min=6, max=35),
        ]
    )