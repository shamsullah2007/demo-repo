from flask import Flask,render_template,url_for,flash,redirect
from form import RegForm

app=Flask(__name__)

app.config["SECRET_KEY"]="86a1121bbb51e87ef093e828566b"

@app.route("/" , methods=["get","post"])
def home():
    return  'this is home page' 

@app.route("/regis" ,methods=["GET","POST"])
def regis():
    form=RegForm()
    if form.validate_on_submit():
        flash(f"account created for {form.username.data}","success")
        redirect(url_for('regis'))

     
    return render_template("regis.html" ,form=form)

if __name__=="__main__":
    app.run(debug=True)