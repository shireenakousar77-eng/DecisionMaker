from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_score(p):
    return (
        p['benefit'] * 3 +
        p['usage'] * 2 +
        p['range'] * 2 -
        p['risk'] * 2 -
        p['cost']
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    projects = request.json['projects']

    best = None
    best_score = -9999

    for p in projects:
        score = calculate_score(p)
        p['score'] = score
        if score > best_score:
            best_score = score
            best = p

    return jsonify({"best": best})

if __name__ == '__main__':
    app.run(debug=True)