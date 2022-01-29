from flask import Flask

app = Flask('YourNal')
app.config['SECRET_KEY'] = 'very simple secret key'
