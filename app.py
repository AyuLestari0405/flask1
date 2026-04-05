from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ======================== SLEEP DEBT CALCULATOR FUNCTIONS ========================

def calculate_sleep_debt(hours_needed, hours_actual, days_per_month=30, months_per_year=12):
    """
    Menghitung utang tidur dan dampak pada kapasitas otak
    
    Args:
        hours_needed: Jam tidur yang direkomendasikan per malam (biasanya 8 jam)
        hours_actual: Jam tidur aktual per malam
        days_per_month: Hari per bulan (default 30)
        months_per_year: Bulan per tahun (default 12)
    
    Returns:
        dict: Hasil perhitungan sleep debt
    """
    
    # Validasi input
    if hours_needed <= 0 or hours_actual < 0:
        return {"error": "Input tidak valid. Jam tidur harus lebih dari 0."}
    
    if hours_actual > hours_needed:
        return {"message": "Wow! Anda tidur lebih dari yang direkomendasikan. Tetap jaga keseimbangan!"}
    
    # Hitung kekurangan tidur per malam
    sleep_deficit_per_night = hours_needed - hours_actual
    
    # Hitung hari dalam setahun
    days_per_year = days_per_month * months_per_year
    actual_working_days = days_per_year
    
    # Hitung total utang tidur per tahun (dalam jam)
    total_sleep_debt_per_year_hours = sleep_deficit_per_night * actual_working_days
    total_sleep_debt_per_year_days = total_sleep_debt_per_year_hours / 24
    
    # Hitung dampak pada cognition
    impaired_cognition_days = (sleep_deficit_per_night / 1.0) * 45
    
    # Hitung persentase kapasitas otak yang hilang
    cognition_loss_percentage = (impaired_cognition_days / actual_working_days) * 100
    
    results = {
        "success": True,
        "hours_needed": hours_needed,
        "hours_actual": hours_actual,
        "sleep_deficit_per_night": round(sleep_deficit_per_night, 2),
        "total_sleep_debt_per_year_hours": round(total_sleep_debt_per_year_hours, 2),
        "total_sleep_debt_per_year_days": round(total_sleep_debt_per_year_days, 2),
        "impaired_cognition_days": round(impaired_cognition_days, 1),
        "cognition_loss_percentage": round(cognition_loss_percentage, 1),
        "days_per_year": actual_working_days,
        "shock_factor": f"Karena kurang tidur {sleep_deficit_per_night:.1f} jam tiap malam, secara mental kamu menghabiskan {round(impaired_cognition_days, 0):.0f} hari setahun dalam kondisi 'setengah sadar'."
    }
    
    return results

# ======================== SLEEP DEBT CALCULATOR ROUTES ========================

@app.route("/sleep-debt")
def sleep_debt_index():
    return render_template("sleep_debt/index.html")

@app.route("/sleep-debt/calculate", methods=["POST"])
def sleep_debt_calculate():
    """Endpoint untuk menghitung sleep debt"""
    try:
        data = request.get_json()
        hours_needed = float(data.get("hours_needed", 8))
        hours_actual = float(data.get("hours_actual", 5))
        
        result = calculate_sleep_debt(hours_needed, hours_actual)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 400

@app.route("/sleep-debt/info")
def sleep_debt_info():
    info_data = {
        "title": "Tentang Sleep Debt Calculator",
        "description": "Kalkulator ini menghitung akumulasi 'utang tidur' Anda dan memprediksi dampaknya terhadap fungsi kognitif.",
        "how_it_works": [
            "Input berapa jam tidur yang Anda butuhkan per malam (rekomendasi: 8 jam)",
            "Input berapa jam tidur aktual Anda per malam",
            "Sistem akan menghitung total utang tidur setahun dan dampaknya",
            "Hasil menunjukkan berapa hari dalam setahun Anda berfungsi dengan impaired cognition"
        ],
        "research": "Penelitian menunjukkan bahwa 1 jam kurang tidur setiap malam setara dengan 45 hari dalam setahun berfungsi dengan kapasitas otak yang setara dengan orang mabuk (BAC 0.05%)."
    }
    return render_template("sleep_debt/info.html", info=info_data)

# ======================== FLASK HELLO APP ROUTES ========================

# Route Home
@app.route("/")
def home():
    return render_template('home.html')

# Route About
@app.route('/about')
def about():
    return render_template('about.html')

# Route Nama Dinamis
@app.route('/nama/<string:nama>')
def getnama(nama):
    return f"Nama anda adalah {nama}"

# Route User dengan Variabel
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

# Route User ID
@app.route('/user/<int:user_id>')
def user_id(user_id):
    return f"User ID: {user_id}"

# Route Profile
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

# Route Data Dictionary
@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

# Route Users List
@app.route('/users')
def users():
    user_list = ["Ali", "Budi", "Citra", "Dewi"]
    return render_template('users.html', users=user_list)

# Route Users dengan Role (Admin dan User)
@app.route('/users-role')
def users_role():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list, show_role=True)

# Route Nilai Berdasarkan Score
@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)

# Route Mahasiswa
@app.route('/mahasiswa')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "Ali", "nilai": 92},
        {"nama": "Budi", "nilai": 80},
        {"nama": "Citra", "nilai": 65},
        {"nama": "Dewi", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)

if __name__ == "__main__":
    app.run(debug=True)
