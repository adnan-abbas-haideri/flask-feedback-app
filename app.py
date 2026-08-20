from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (

        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        feedback TEXT

    )
    """)

    conn.commit()
    conn.close()


create_table()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    feedback = request.form["feedback"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO feedback(name,email,feedback) VALUES(%s,%s,%s)",
        (name, email, feedback)
    )

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        success="Feedback Submitted Successfully!"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
