from flask import Flask, render_template, request

app = Flask(__name__)


def hitung_net_profit(laba_bersih, pendapatan):
    try:
        hasil = (laba_bersih / pendapatan) * 100
        return round(hasil, 2)
    except ZeroDivisionError:
        return 0


@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None

    if request.method == 'POST':
        laba_bersih = float(request.form['laba_bersih'])
        pendapatan = float(request.form['pendapatan'])
        hasil = hitung_net_profit(laba_bersih, pendapatan)

    return render_template('index.html', hasil=hasil)


if __name__ == '__main__':
    app.run(debug=True)
