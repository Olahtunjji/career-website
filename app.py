from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'description': 'Analyze data and make decisions',
   },
  {
    'id': 2,
    'title': 'Data Clerk',
    'description': 'Enter data into a database',
   },
{
  'id': 3,
  'title': 'Data Scientist',
  'description': 'create models and make predictions',
  },
{
  'id': 4,
  'title': 'Data Rect',
  'description': 'rectify data and make it clean',
 }
]

@app.route('/')
def home():
  return render_template('home.html',
                        projects=PROJECTS,
                        company_name='Replit')
@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True,)
  