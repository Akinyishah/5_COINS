from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')          #func 1
def home():              #func 2   
    return render_template("index.html")


@app.route('/menu')
def menu():
        return render_template("menu.html")

#running an application one has to tell FLASK 
app.run(debug=True)