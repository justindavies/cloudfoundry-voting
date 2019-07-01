# import dependencies
import os
from flask import Flask
from flask import render_template
from flask_static_compress import FlaskStaticCompress



# bootstrap the app
app = Flask(__name__, static_folder="static", template_folder="templates")

compress = FlaskStaticCompress(app)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    user = {'username': 'SUSE'}
    return render_template('index.html', title='Home', user=user)

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)