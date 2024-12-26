import sys
import numpy as np
import pyqtgraph as pg
import pyads

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from modify import update

class LivePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        # Abre conexão com PLC
        self.plc = pyads.Connection('192.168.71.1.1.1', pyads.PORT_TC3PLC1)
        self.plc.open()

        # Inicialização da interface gráfica
        self.setWindowTitle('Gráfico em Tempo Real')
        self.setGeometry(350, 100, 1280, 768)

        # Layout principal
        layout = QVBoxLayout()

        # Criar o widget de gráficos
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        # Configurar o gráfico
        self.plot_widget.setTitle("Gráfico")
        self.plot_widget.setLabel('left', 'Amplitude')
        self.plot_widget.setLabel('bottom', 'Tempo')

        # Pega tamanho do array
        self.size = self.plc.read_by_name('MAIN.Size', pyads.PLCTYPE_INT)

        # Gerar os dados para o gráfico
        self.x = [-0.01*i for i in range(1,self.size+1,1)]  # Eixo X fixo (tempo)
        self.y = np.zeros(self.size)   # Valores iniciais

        # Plotar 
        self.plot_curve = self.plot_widget.plot(self.x, self.y, pen='r')

        # Configurar um timer para atualizar o gráfico
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(30) 

        # Definir o layout da janela
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_plot(self):
        """Atualiza o gráfico a cada tick do timer"""
        value = list(self.plc.read_by_name('MAIN.Buffer_y', pyads.PLCTYPE_REAL * self.size))

        self.y = update(value)

        self.plot_curve.setData(self.x, self.y)  # Atualiza o gráfico com os novos dados

    def closeEvent(self, event):
        """Fechar a conexão do PLC ao sair"""
        self.plc.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LivePlot()
    window.show()
    sys.exit(app.exec_())


