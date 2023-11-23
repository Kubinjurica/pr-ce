from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    Markup,
    escape,
    flash,
)
import functools


app = Flask(__name__)
app.secret_key = b"totoj e zceLa n@@@hodny retezec nejlep os.urandom(24)"
app.secret_key = b"x6\x87j@\xd3\x88\x0e8\xe8pM\x13\r\xafa\x8b\xdbp\x8a\x1f\xd41\xb8"

@app.route("/", methods=["GET"])
def root():
    return render_template("base.html")

@app.route("/kocka/")
def kocka():
    return render_template("kocka.html")

@app.route("/pes/")
def pes():
    return render_template("pes.html")

@app.route("/krysa/")
def krysa():
    return render_template("krysa.html")

@app.route("/admin/")
def admin():
    return render_template("admin.html")

@app.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")
@app.route("/login/", methods = ["POST"])
def login_post():
    jmeno = request.form.get("jmeno", "")
    heslo = request.form.get("heslo", "")
    url = request.args.get("url", "")
    if jmeno and heslo == "69420":
        session["user"] = jmeno
        flash("Jsi přihlášen!", "success")
        if url:
            return redirect(url)
        else:
            return redirect(url_for("root"))

    else:
        flash("Nesprávné přihlašovací údaje!", "error")
    return redirect(url_for("login", url = url))


@app.route("/logout/")
def logout():
    session.pop("user", None)
    flash("Byl jsi odhlášen!", "success")
    return redirect(url_for("root"))
