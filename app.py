from flask import Flask, render_template, request, redirect, url_for, session
from app.main import generateImg

app = Flask(__name__)
app.secret_key = "key"  

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/generate", methods=["POST", "GET"])
def generate():
    prmpt = ""
    sz = ""
    if request.method == "POST":
        if request.form["prompt"] and request.form["size"]:
            prmpt = request.form["prompt"]
            sz = request.form["size"]
            session["prompt"] = prmpt
            session["size"] = sz
            return redirect(url_for("success"))
    
    
    return redirect(url_for("home"))
        
    
    
@app.route("/success")
def success():
    if "prompt" in session:
        prmpt = session["prompt"]
        sz = session["size"]
        url = generateImg(prmpt, sz)
        session.pop("prompt", None)  
        session.pop("size", None)

        return render_template("index.html", imgUrl = url)
    else:
        return redirect(url_for("home"))

# run the app
if __name__ == "__main__":
    app.run()
