from flask import Flask, render_template, request, redirect

app = Flask(__name__)

projects = []

def calculate_score(p):
    return (
        p['benefit'] * 0.4 +
        p['usage'] * 0.3 -
        p['cost'] * 0.2 -
        p['risk'] * 0.1
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    global projects
    best = None

    if request.method == 'POST':
        project = {
            'name': request.form['name'],
            'cost': float(request.form['cost']),
            'benefit': float(request.form['benefit']),
            'risk': float(request.form['risk']),
            'usage': float(request.form['usage'])
        }

        project['score'] = round(calculate_score(project), 2)
        projects.append(project)

    if projects:
        best = max(projects, key=lambda x: x['score'])

    return render_template('index.html', projects=projects, best=best)


# ✅ VERY IMPORTANT (CLEAR ROUTE)
@app.route('/clear', methods=['POST'])
def clear():
    global projects
    projects.clear()   # better than projects = []
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)