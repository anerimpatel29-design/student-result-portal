from flask import Flask, render_template, request

app = Flask(__name__)

students = {
    "101": {"name": "Rahul", "marks": 85, "grade": "A"},
    "102": {"name": "Priya", "marks": 78, "grade": "B"},
    "103": {"name": "Amit", "marks": 92, "grade": "A+"}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    roll = request.form["roll"]
    student = students.get(roll)
    return render_template("result.html", student=student, roll=roll)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)