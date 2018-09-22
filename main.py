from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action='/caesar' method="post">
    <label for="rotate-by">Rotate by:</label>
    <input type="text" name="rot" value="0">
    <textarea name="text">{0}</textarea>
    <input type="submit" value="Submit">
    </body>
</html>


"""

@app.route("/")
def index():
    return form.format("")

@app.route("/caesar", methods=['POST'])
def encrypt():    
    user_rotate_num = request.form[('rot')]
    rotate_by = int(user_rotate_num)
    user_text = request.form['text']
    encrypted_string = rotate_string(user_text,rotate_by)
    return form.format(encrypted_string)

app.run()