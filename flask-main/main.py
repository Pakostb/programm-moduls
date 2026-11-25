from flask import Flask, request, render_template, session, redirect, url_for
from database import Database

app = Flask(__name__)
app.secret_key = "change-me-secret-key-123"

db = Database()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # POST
    name = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not password:
        return render_template("register.html", error="Заполните все поля")

    try:
        db.create_user(name, password)
    except Exception:
        # Обычно IntegrityError при дубликате имени
        return render_template("register.html", error="Имя уже занято или ошибка БД")

    # Успех → сохраняем в сессию и на профиль
    session["username"] = name
    return redirect(url_for("profile"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    name = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not password:
        return render_template("login.html", error="Введите имя и пароль")

    user = db.get_user(name)
    if user and user["user_password"] == password:
        session["username"] = name
        return redirect(url_for("profile"))

    return render_template("login.html", error="Неверное имя или пароль")


@app.route("/profile")
def profile():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
