from flask import Flask, render_template, request
from model import recommend_universities

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        inputs = {
            "gpa": float(request.form["gpa"]),
            "ielts": float(request.form["ielts"]),
            "sat": int(request.form["sat"]),
            "ap": int(request.form["ap"]),
            "budget": int(request.form["budget"]),
            "major": request.form["major"],
            "climate": request.form["climate"],
            "project_level": request.form["project_level"]
        }
        results = recommend_universities(inputs)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
