from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/blog")
def blog():
    posts=[
        {"title":"Flask mystory cource","auther":"chatgpt","content":"backend web dev"},
        {"title":"data science","auther":"chatgpt","content":"machine learning"}

    ]
    return render_template("blog.html",posts=posts)

if __name__=="__main__":
    app.run(debug=True)