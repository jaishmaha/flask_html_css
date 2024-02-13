from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route('/student')
def student():
    Student_list = [{"Name":"Sivapackia","Age":22 ,"Roll_NO": 101, "Marks":[90,75,80,98,65]},
                        {"Name":"Siva","Age":21 ,"Roll_NO": 102, "Marks":[90,75,80,78,99]},
                        {"Name":"Vilobin","Age":21 ,"Roll_NO": 103, "Marks":[94,75,80,88,35]},
                        {"Name":"Mahadevi","Age":27 ,"Roll_NO": 104, "Marks":[70,85,80,98,35]},          
                        {"Name":"Nisha","Age":23 ,"Roll_NO": 105, "Marks":[90,75,85,98,35]},
                        {"Name":"Vaisali","Age":27 ,"Roll_NO": 106, "Marks":[80,98,35,90,75]},
                        {"Name":"Vijay","Age":22 ,"Roll_NO": 107, "Marks":[90,80,98,35,75]},
                        {"Name":"Mohamed Ismail","Age":22 ,"Roll_NO": 108, "Marks":[75,80,90,98,35]},
                        ]
    return render_template("student.html",student=Student_list)

if __name__ == "__main__":
    app.run(debug=True)
