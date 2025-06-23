from flask import Flask, render_template, request
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy
from fuzzy_logic import create_fuzzy_system, define_rules
from skfuzzy import control as ctrl

app = Flask(__name__)

def plot_membership(variable, title, filename, input_value=None):
    """
    Membuat dan menyimpan plot fungsi keanggotaan untuk sebuah variabel fuzzy.
    Secara opsional, tambahkan penanda input pengguna dan derajat keanggotaannya.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    
    for term_name, term in variable.terms.items():
        ax.plot(variable.universe, term.mf, label=term_name)

    if input_value is not None:
        membership_degrees = {
            term: skfuzzy.interp_membership(variable.universe, variable[term].mf, input_value)
            for term in variable.terms
        }

        for term, mu in membership_degrees.items():
            if mu > 0:
                ax.plot([input_value, input_value], [0, mu], 'r--', linewidth=1.5)
                ax.plot([0, input_value], [mu, mu], 'r--', linewidth=1.5)
                ax.plot(input_value, mu, 'ro', markersize=5)

        y_ticks = sorted(list(set(list(ax.get_yticks()) + [mu for mu in membership_degrees.values() if mu > 0])))
        ax.set_yticks(y_ticks)

    ax.set_ylabel("Derajat Keanggotaan (μ)")
    ax.set_xlabel(title)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_ylim(0, 1.05)
    ax.set_xlim(left=0, right=variable.universe.max())

    output_dir = 'static/images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    plt.savefig(os.path.join(output_dir, filename))
    plt.close(fig)

@app.route('/', methods=['GET', 'POST'])
def index():
    luas_rumah, daya_listrik, perlengkapan_elektronik, pendapatan_ekonomi, biaya_pemakaian = create_fuzzy_system()
    rules = define_rules(luas_rumah, daya_listrik, perlengkapan_elektronik, pendapatan_ekonomi, biaya_pemakaian)

    if request.method == 'POST':
        input_luas_rumah = float(request.form['luas_rumah'])
        input_daya_listrik = float(request.form['daya_listrik'])
        input_perlengkapan_elektronik = float(request.form['perlengkapan_elektronik'])
        input_pendapatan_ekonomi = float(request.form['pendapatan_ekonomi'])

        plot_membership(luas_rumah, 'Luas Rumah', 'luas_rumah.png', input_value=input_luas_rumah)
        plot_membership(daya_listrik, 'Daya Listrik', 'daya_listrik.png', input_value=input_daya_listrik)
        plot_membership(perlengkapan_elektronik, 'Perlengkapan Elektronik', 'perlengkapan_elektronik.png', input_value=input_perlengkapan_elektronik)
        plot_membership(pendapatan_ekonomi, 'Pendapatan Ekonomi', 'pendapatan_ekonomi.png', input_value=input_pendapatan_ekonomi)

        biaya_pemakaian_ctrl = ctrl.ControlSystem(rules)
        biaya_pemakaian_sim = ctrl.ControlSystemSimulation(biaya_pemakaian_ctrl)
        biaya_pemakaian_sim.input['luas_rumah'] = input_luas_rumah
        biaya_pemakaian_sim.input['daya_listrik'] = input_daya_listrik
        biaya_pemakaian_sim.input['perlengkapan_elektronik'] = input_perlengkapan_elektronik
        biaya_pemakaian_sim.input['pendapatan_ekonomi'] = input_pendapatan_ekonomi
        biaya_pemakaian_sim.compute()
        hasil_biaya = round(biaya_pemakaian_sim.output['biaya_pemakaian'], 2)

        biaya_pemakaian.view(sim=biaya_pemakaian_sim)
        plt.savefig('static/images/hasil_biaya_pemakaian.png')
        plt.close()

        return render_template('index.html', hasil_biaya=hasil_biaya, plot_hasil=True)
    
    else: # Ini adalah request GET (saat halaman pertama kali dibuka)
        plot_membership(luas_rumah, 'Luas Rumah', 'luas_rumah.png')
        plot_membership(daya_listrik, 'Daya Listrik', 'daya_listrik.png')
        plot_membership(perlengkapan_elektronik, 'Perlengkapan Elektronik', 'perlengkapan_elektronik.png')
        plot_membership(pendapatan_ekonomi, 'Pendapatan Ekonomi', 'pendapatan_ekonomi.png')
        return render_template('index.html', plot_hasil=False)

if __name__ == '__main__':
    app.run(debug=True)