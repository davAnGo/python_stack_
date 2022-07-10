from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("create.html", users = users)

@app.route("/create_user", methods=["POST"])
def create_user():
    data ={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/read")

@app.route("/read")
def read():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", users = users)
            
if __name__ == "__main__":
    app.run(debug=True)
