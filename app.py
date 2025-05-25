from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
data = []

kategorier = ['Mat', 'Ferie', 'Klær', 'Sport', 'Internett', 'Hus', 'Bil', 'Annet']

@app.route('/')
def index():
    saldo = sum([x['beløp'] for x in data])
    return render_template('index.html', data=data, saldo=saldo, kategorier=kategorier)

@app.route('/legg_til', methods=['POST'])
def legg_til():
    try:
        beløp = float(request.form['beløp'])
        kategori = request.form['kategori']
        tekst = request.form['tekst'] or '-'
        type_ = request.form['type']

        if type_ == 'Utgift':
            beløp = -beløp

        data.append({'beløp': beløp, 'kategori': kategori, 'tekst': tekst})
    except:
        pass
    return redirect(url_for('index'))

@app.route('/nullstill')
def nullstill():
    global data
    data = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
