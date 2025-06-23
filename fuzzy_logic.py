import numpy as np
import skfuzzy
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

def create_fuzzy_system():
    # Definisi variabel linguistik
    luas_rumah = ctrl.Antecedent(np.arange(0, 251, 1), 'luas_rumah')
    daya_listrik = ctrl.Antecedent(np.arange(0, 2201, 1), 'daya_listrik')
    perlengkapan_elektronik = ctrl.Antecedent(np.arange(0, 19, 1), 'perlengkapan_elektronik')
    pendapatan_ekonomi = ctrl.Antecedent(np.arange(0, 10.5, 0.5), 'pendapatan_ekonomi')
    biaya_pemakaian = ctrl.Consequent(np.arange(0, 1201, 50), 'biaya_pemakaian')

    # Himpunan fuzzy untuk setiap variabel
    # Luas Rumah
    luas_rumah['standard'] = skfuzzy.trapmf(luas_rumah.universe, [0, 0, 15, 55])
    luas_rumah['medium'] = skfuzzy.trimf(luas_rumah.universe, [40, 80, 120])
    luas_rumah['besar'] = skfuzzy.trapmf(luas_rumah.universe, [105, 145, 250, 250])

    # Daya Listrik
    daya_listrik['rendah'] = skfuzzy.trapmf(daya_listrik.universe, [0, 0, 400, 900])
    daya_listrik['sedang'] = skfuzzy.trimf(daya_listrik.universe, [400, 900, 1400])
    daya_listrik['tinggi'] = skfuzzy.trapmf(daya_listrik.universe, [900, 1400, 2200, 2200])

    # Perlengkapan Elektronik
    perlengkapan_elektronik['sedikit'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [0, 0, 5, 7])
    perlengkapan_elektronik['normal'] = skfuzzy.trimf(perlengkapan_elektronik.universe, [5, 9, 13])
    perlengkapan_elektronik['banyak'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [11, 13, 18, 18])

    # Pendapatan Ekonomi
    pendapatan_ekonomi['rendah'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [0, 0, 1, 2.5])
    pendapatan_ekonomi['sedang'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [2, 4, 4.5, 6.5])
    pendapatan_ekonomi['tinggi'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [6, 7.5, 10, 10])

    # Biaya Pemakaian
    biaya_pemakaian['rendah'] = skfuzzy.trapmf(biaya_pemakaian.universe, [0, 0, 200, 300])
    biaya_pemakaian['sedang'] = skfuzzy.trapmf(biaya_pemakaian.universe, [200, 300, 400, 500])
    biaya_pemakaian['tinggi'] = skfuzzy.trapmf(biaya_pemakaian.universe, [400, 500, 1200, 1200])

    return luas_rumah, daya_listrik, perlengkapan_elektronik, pendapatan_ekonomi, biaya_pemakaian

def define_rules(luas_rumah, daya_listrik, perlengkapan_elektronik, pendapatan_ekonomi, biaya_pemakaian):
  # No. | Luas Rumah | Daya Listrik | Perlengkapan Elektronik | Pendapatan Ekonomi | Biaya Pemakaian
  # 1.  STANDAR   RENDAH  SEDIKIT   RENDAH  RENDAH
  R1=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 2.  STANDAR   RENDAH  SEDIKIT   SEDANG  RENDAH
  R2=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

  # 3.  STANDAR   RENDAH  SEDIKIT   TINGGI  RENDAH
  R3=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['rendah'])

  # 4.  STANDAR   RENDAH  NORMAL  RENDAH  RENDAH
  R4=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 5.  STANDAR   RENDAH  NORMAL  SEDANG  RENDAH
  R5=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

  # 6.  STANDAR   RENDAH  NORMAL  TINGGI  SEDANG
  R6=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 7.  STANDAR   RENDAH  BANYAK  RENDAH  RENDAH
  R7=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 8.  STANDAR   RENDAH  BANYAK  SEDANG  SEDANG
  R8=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 9.  STANDAR   RENDAH  BANYAK  TINGGI  SEDANG
  R9=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 10.  STANDAR   SEDANG  SEDIKIT   RENDAH  RENDAH
  R10=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 11.  STANDAR   SEDANG  SEDIKIT   SEDANG  RENDAH
  R11=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

  # 12.  STANDAR   SEDANG  SEDIKIT   TINGGI  SEDANG
  R12=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 13.  STANDAR   SEDANG  NORMAL  RENDAH  RENDAH
  R13=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 14.  STANDAR   SEDANG  NORMAL  SEDANG  SEDANG
  R14=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 15.  STANDAR   SEDANG  NORMAL  TINGGI  SEDANG
  R15=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 16.  STANDAR   SEDANG  BANYAK  RENDAH  SEDANG
  R16=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 17.  STANDAR   SEDANG  BANYAK  SEDANG  SEDANG
  R17=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 18.  STANDAR   SEDANG  BANYAK  TINGGI  TINGGI
  R18=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 19.  STANDAR   TINGGI  SEDIKIT   RENDAH  SEDANG
  R19=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 20.  STANDAR   TINGGI  SEDIKIT   SEDANG  SEDANG
  R20=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 21.  STANDAR   TINGGI  SEDIKIT   TINGGI  SEDANG
  R21=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 22.  STANDAR   TINGGI  NORMAL  RENDAH  SEDANG
  R22=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 23.  STANDAR   TINGGI  NORMAL  SEDANG  TINGGI
  R23=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 24.  STANDAR   TINGGI  NORMAL  TINGGI  TINGGI
  R24=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 25.  STANDAR   TINGGI  BANYAK  RENDAH  TINGGI
  R25=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

  # 26.  STANDAR   TINGGI  BANYAK  SEDANG  TINGGI
  R26=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 27.  STANDAR   TINGGI  BANYAK  TINGGI  TINGGI
  R27=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 28.  MEDIUM   RENDAH  SEDIKIT   RENDAH  RENDAH
  R28=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 29.  MEDIUM   RENDAH  SEDIKIT   SEDANG  RENDAH
  R29=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

  # 30.  MEDIUM   RENDAH  SEDIKIT   TINGGI  SEDANG
  R30=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 31.  MEDIUM   RENDAH  NORMAL  RENDAH  RENDAH
  R31=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 32.  MEDIUM   RENDAH  NORMAL  SEDANG  SEDANG
  R32=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 33.  MEDIUM   RENDAH  NORMAL  TINGGI  SEDANG
  R33=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 34.  MEDIUM   RENDAH  BANYAK  RENDAH  SEDANG
  R34=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 35.  MEDIUM   RENDAH  BANYAK  SEDANG  SEDANG
  R35=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 36.  MEDIUM   RENDAH  BANYAK  TINGGI  TINGGI
  R36=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 37.  MEDIUM   SEDANG  SEDIKIT   RENDAH  RENDAH
  R37=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

  # 38.  MEDIUM   SEDANG  SEDIKIT   SEDANG  SEDANG
  R38=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 39.  MEDIUM   SEDANG  SEDIKIT   TINGGI  SEDANG
  R39=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 40.  MEDIUM   SEDANG  NORMAL  RENDAH  SEDANG
  R40=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 41.  MEDIUM   SEDANG  NORMAL  SEDANG  SEDANG
  R41=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 42.  MEDIUM   SEDANG  NORMAL  TINGGI  TINGGI
  R42=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 43.  MEDIUM   SEDANG  BANYAK  RENDAH  SEDANG
  R43=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 44.  MEDIUM   SEDANG  BANYAK  SEDANG  TINGGI
  R44=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 45.  MEDIUM   SEDANG  BANYAK  TINGGI  TINGGI
  R45=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 46.  MEDIUM   TINGGI  SEDIKIT   RENDAH  SEDANG
  R46=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 47.  MEDIUM   TINGGI  SEDIKIT   SEDANG  SEDANG
  R47=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 48.  MEDIUM   TINGGI  SEDIKIT   TINGGI  TINGGI
  R48=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 49.  MEDIUM   TINGGI  NORMAL  RENDAH  SEDANG
  R49=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 50.  MEDIUM   TINGGI  NORMAL  SEDANG  TINGGI
  R50=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 51.  MEDIUM   TINGGI  NORMAL  TINGGI  TINGGI
  R51=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 52.  MEDIUM   TINGGI  BANYAK  RENDAH  TINGGI
  R52=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

  # 53.  MEDIUM   TINGGI  BANYAK  SEDANG  TINGGI
  R53=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 54.  MEDIUM   TINGGI  BANYAK  TINGGI  TINGGI
  R54=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 55.  BESAR   RENDAH  SEDIKIT   RENDAH  SEDANG
  R55=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 56.  BESAR   RENDAH  SEDIKIT   SEDANG  SEDANG
  R56=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 57.  BESAR   RENDAH  SEDIKIT   TINGGI  SEDANG
  R57=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

  # 58.  BESAR   RENDAH  NORMAL  RENDAH  SEDANG
  R58=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 59.  BESAR   RENDAH  NORMAL  SEDANG  SEDANG
  R59=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 60.  BESAR   RENDAH  NORMAL  TINGGI  TINGGI
  R60=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 61.  BESAR   RENDAH  BANYAK  RENDAH  SEDANG
  R61=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 62.  BESAR   RENDAH  BANYAK  SEDANG  TINGGI
  R62=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 63.  BESAR   RENDAH  BANYAK  TINGGI  TINGGI
  R63=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 64.  BESAR   SEDANG  SEDIKIT   RENDAH  SEDANG
  R64=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 65.  BESAR   SEDANG  SEDIKIT   SEDANG  SEDANG
  R65=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

  # 66.  BESAR   SEDANG  SEDIKIT   TINGGI  TINGGI
  R66=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 67.  BESAR   SEDANG  NORMAL  RENDAH  SEDANG
  R67=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 68.  BESAR   SEDANG  NORMAL  SEDANG  TINGGI
  R68=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 69.  BESAR   SEDANG  NORMAL  TINGGI  TINGGI
  R69=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 70.  BESAR   SEDANG  BANYAK  RENDAH  TINGGI
  R70=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

  # 71.  BESAR   SEDANG  BANYAK  SEDANG  TINGGI
  R71=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 72.  BESAR   SEDANG  BANYAK  TINGGI  TINGGI
  R72=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 73.  BESAR   TINGGI  SEDIKIT   RENDAH  SEDANG
  R73=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

  # 74.  BESAR   TINGGI  SEDIKIT   SEDANG  TINGGI
  R74=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 75.  BESAR   TINGGI  SEDIKIT   TINGGI  TINGGI
  R75=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 76.  BESAR   TINGGI  NORMAL  RENDAH  TINGGI
  R76=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

  # 77.  BESAR   TINGGI  NORMAL  SEDANG  TINGGI
  R77=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 78.  BESAR   TINGGI  NORMAL  TINGGI  TINGGI
  R78=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

  # 79.  BESAR   TINGGI  BANYAK  RENDAH  TINGGI
  R79=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

  # 80.  BESAR   TINGGI  BANYAK  SEDANG  TINGGI
  R80=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

  # 81.  BESAR   TINGGI  BANYAK  TINGGI  TINGGI
  R81=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])


  rules = [R1, R2, R3, R4, R5, R6, R7, R8, R9,
         R10, R11, R12, R13, R14, R15, R16, R17, R18,
         R19, R20, R21, R22, R23, R24, R25, R26, R27,
         R28, R29, R30, R31, R32, R33, R34, R35, R36,
         R37, R38, R39, R40, R41, R42, R43, R44, R45,
         R46, R47, R48, R49, R50, R51, R52, R53, R54,
         R55, R56, R57, R58, R59, R60, R61, R62, R63,
         R64, R65, R66, R67, R68, R69, R70, R71, R72,
         R73, R74, R75, R76, R77, R78, R79, R80, R81]

  return rules

def plot_membership(variable, title, filename):
    fig, ax = plt.subplots(figsize=(8, 3))
    for term_name, term in variable.terms.items():
        ax.plot(variable.universe, term.mf, label=term_name)
    ax.set_title(title)
    ax.legend()
    plt.savefig(f'static/images/{filename}')
    plt.close(fig)