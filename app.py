from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="manisha@22",
        database="student_performance",
        use_pure=True
    )


@app.route("/", methods=["GET", "POST"])
def login():

    print("REQUEST METHOD:", request.method)

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        print("EMAIL:", email)
        print("PASSWORD:", password)

        try:
            db = get_db_connection()
            cursor = db.cursor(dictionary=True)

            query = """
                SELECT * FROM students
                WHERE email = %s AND password = %s
            """

            cursor.execute(query, (email, password))
            student = cursor.fetchone()

            print("STUDENT:", student)

            cursor.close()
            db.close()

            if student:
                print("LOGIN SUCCESS")
                return redirect(url_for("dashboard"))

            print("LOGIN FAILED")
            return render_template(
                "login.html",
                error="Invalid Email or Password"
            )

        except Exception as e:
            print("DATABASE ERROR:", e)
            return render_template(
                "login.html",
                error="Database connection error"
            )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/students")
def students():
    return render_template("students.html")


@app.route("/marks")
def marks():
    return render_template("marks.html")


@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


@app.route("/performance")
def performance():
    return render_template("performance.html")


if __name__ == "__main__":
    app.run(debug=True)