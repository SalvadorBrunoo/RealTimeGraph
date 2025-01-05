import numpy as np
from scipy.signal import firwin, lfilter
import matplotlib.pyplot as plt

def update(signal:list, n):

    if n > 0:
        signal = filtro(signal, 10, 100, num_taps=n+1)

    new_signal = []

    a = (4980000-7060000) / 10
    b = 10 - 7060000*a

    for x in signal:
        y = x*a + b
        new_signal += [y]
    
    signal = new_signal

    return signal

# Função para criar um filtro FIR passa-baixa
def filtro(dados, cutoff, fs, num_taps=51):

    # Design do filtro FIR com janela de Hamming
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    coeficientes = firwin(num_taps, normal_cutoff, window="hamming")
    # Aplicação do filtro
    dados_filtrados = lfilter(coeficientes, 1.0, dados)

    return dados_filtrados[(num_taps-1):]
