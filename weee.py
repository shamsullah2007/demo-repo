from flask import Flask,url_for,render_template,request,redirect
from datetime import datetime

app=Flask(__name__)
@app.route("/contact",methods=["GET","POST"])
def contact():
    errors=[]
    name=""
    email="" 
    message=""
    if request.method=="POST":
        name=request.form.get('name',"").strip()
        email=request.form.get("email",'').strip()
        message=request.form.get("message","").strip()

        if not name:
            errors.append("enter your name")
        if not email or "@" not in email or "gmail.com" not in email:
            errors.append("enter a vaild email")
        if not message or len(message)<5:
            errors.append("message must be at leasrt 5 charachters")
        if not errors:
            return "submit succesfully"
            
    
    return render_template("contact.html" ,email=email,message=message,name=name,errors=errors)

@app.route("/")
def home():
    return render_template("base.html")

posts=[]

@app.route("/newpost" ,methods=["GET","POST"])
def newpost():
    errors=[]
    title=content=author=""
    if request.method=="post":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        content = request.form.get("content", "").strip()
        if not title or title is int:
            errors.append("enter a vailed name")
        if not content and len(content)<10 and len(content)>100:
            errors.append("fille in the range of 10 to 100")
        if not author or 18>len(author)>2:
            errors.append("author name must be in range of 2 to 18")
        if not errors:
            posts.append({
                "author": author,
                "title":title,
                "content":content,
                "created_at":datetime.utcnow()




            })
            return redirect({url_for(contact)})
    return render_template("new_post.html" ,errors=errors,title=title,author=author,content=content)







if __name__=="__main__":
    app.run(debug=True)   