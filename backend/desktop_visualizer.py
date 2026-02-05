import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout

class CSVVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equipment CSV Visualizer")

        layout = QVBoxLayout()

        self.button = QPushButton("Upload CSV")
        self.button.clicked.connect(self.load_csv)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def load_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_name:
            df = pd.read_csv(file_name)
            counts = df["Type"].value_counts()

            counts.plot(kind="pie", autopct="%1.1f%%")
            plt.title("Equipment Distribution")
            plt.show()

app = QApplication(sys.argv)
window = CSVVisualizer()
window.show()
sys.exit(app.exec_())
