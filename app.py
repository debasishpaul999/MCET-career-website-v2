from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[{
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '10,00,000'
},
{
    'id':2,
    'title': 'Data Scientist',
    'location': 'Pune, India',
    'salary': '25,00,000'
},
{
    'id':3,
    'title': 'Software Engineer',
    'location': 'Chennai, India'
},
{
    'id':4,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '12,00,000'
}]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='90', debug=True)