from flask import Flask, render_template, request, jsonify, redirect, url_for, session, make_response
import pandas as pd
import joblib
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=15)

# Identifiants
USER_CREDENTIALS = {
    "churn": "2025"
}

# Chargement des modèles
model = joblib.load("knn_best_f1_model.joblib")
scaler = joblib.load("scaler.joblib")
threshold = joblib.load("knn_best_f1_threshold.joblib")

# Mapping des régions
region_mapping = {
    'DAKAR': 0, 'THIES': 1, 'SAINT-LOUIS': 2, 'LOUGA': 3, 'KAOLACK': 4,
    'DIOURBEL': 5, 'TAMBACOUNDA': 6, 'KOLDA': 7, 'KAFFRINE': 8, 'FATICK': 9,
    'MATAM': 10, 'ZIGUINCHOR': 11, 'SEDHIOU': 12, 'KEDOUGOU': 13
}

# Colonnes attendues
ordered_columns = [
    'REGION', 'MONTANT', 'REVENUE', 'FREQUENCE',
    'DATA_VOLUME', 'ON_NET', 'ORANGE', 'REGULARITY',
    'TOP_PACK', 'FREQ_TOP_PACK'
]

# Anti-retour navigateur
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect(url_for('login'))

    prediction = None
    probability = None
    form_data = {}

    if request.method == 'POST':
        try:
            form_data = {col: float(request.form[col]) for col in ordered_columns}
            form_data["REGION"] = int(request.form["REGION"])
            input_df = pd.DataFrame([[form_data[col] for col in ordered_columns]], columns=ordered_columns)
            input_scaled = scaler.transform(input_df)
            proba = model.predict_proba(input_scaled)[:, 1][0]
            prediction = int(proba >= threshold)
            probability = round(proba, 4)
        except Exception as e:
            print("Erreur de traitement :", e)

    return render_template("index.html", prediction=prediction, probability=probability,
                           regions=region_mapping, form_data=form_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('user', None)  # Déconnexion forcée dès l'accès à /login
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('index'))
        else:
            error = "Identifiants invalides"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    if 'user' not in session:
        return jsonify({"error": "Non autorisé"}), 403
    try:
        input_json = request.get_json()
        if not all(col in input_json for col in ordered_columns):
            return jsonify({"error": "Certaines colonnes sont manquantes"}), 400

        input_df = pd.DataFrame([[input_json[col] for col in ordered_columns]], columns=ordered_columns)
        input_scaled = scaler.transform(input_df)
        proba = model.predict_proba(input_scaled)[:, 1][0]
        prediction = int(proba >= threshold)

        return jsonify({
            "prediction": prediction,
            "probability": round(proba, 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()