from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function untuk menghitung sleep debt
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
    actual_working_days = days_per_year  # Asumsi Anda bekerja setiap hari
    
    # Hitung total utang tidur per tahun (dalam jam)
    total_sleep_debt_per_year_hours = sleep_deficit_per_night * actual_working_days
    total_sleep_debt_per_year_days = total_sleep_debt_per_year_hours / 24
    
    # Hitung dampak pada cognition
    # Penelitian menunjukkan 1 jam kurang tidur ≈ 45 hari setahun berfungsi seperti mabuk
    impaired_cognition_days = (sleep_deficit_per_night / 1.0) * 45
    
    # Hitung persentase kapasitas otak yang hilang
    cognition_loss_percentage = (impaired_cognition_days / actual_working_days) * 100
    
    # Hitung rata-rata jam tertidur per hari dalam setahun yang hilang
    hours_lost_per_day_in_year = sleep_deficit_per_night
    
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

# Route untuk halaman utama
@app.route("/sleep-debt")
def index():
    return render_template("index.html")

# Route untuk menghitung sleep debt
@app.route("/sleep-debt/calculate", methods=["POST"])
def calculate():
    """
    Endpoint untuk menghitung sleep debt
    Menerima JSON dengan parameter:
    - hours_needed: Jam tidur yang direkomendasikan
    - hours_actual: Jam tidur aktual
    """
    try:
        data = request.get_json()
        hours_needed = float(data.get("hours_needed", 8))
        hours_actual = float(data.get("hours_actual", 5))
        
        result = calculate_sleep_debt(hours_needed, hours_actual)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 400

# Route untuk halaman hasil
@app.route("/sleep-debt/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        hours_needed = float(request.form.get("hours_needed", 8))
        hours_actual = float(request.form.get("hours_actual", 5))
        
        calculation = calculate_sleep_debt(hours_needed, hours_actual)
        return render_template("index.html", data=calculation)
    
    return render_template("index.html")

# Route untuk info/documentation
@app.route("/sleep-debt/info")
def info():
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
    return render_template("info.html", info=info_data)

if __name__ == "__main__":
    # Jangan jalankan di sini, gunakan main Flask app
    pass
