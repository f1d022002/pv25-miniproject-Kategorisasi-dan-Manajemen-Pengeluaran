import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QSpinBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QMessageBox, QMenuBar, QMenu
)
from PyQt5.QtCore import Qt


class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker App - Andi Sibwayiq (F1D022002)")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # NIM dan Nama
        self.info_label = QLabel("Nama: Andi Sibwayiq | NIM: F1D022002")
        self.info_label.setStyleSheet("font-weight: bold; color: darkblue;")
        layout.addWidget(self.info_label)

        # Form Input
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Deskripsi Pengeluaran")

        self.category_input = QComboBox()
        self.category_input.addItems(["Makanan", "Transportasi", "Hiburan", "Lainnya"])

        self.amount_input = QSpinBox()
        self.amount_input.setMaximum(1000000)
        self.amount_input.setPrefix("Rp ")

        # Button
        self.add_button = QPushButton("Tambah Pengeluaran")
        self.add_button.setStyleSheet("background-color: #3cb371; color: white; font-weight: bold")
        self.add_button.clicked.connect(self.add_expense)

        # Layout Form
        form_layout = QHBoxLayout()
        form_layout.addWidget(self.desc_input)
        form_layout.addWidget(self.category_input)
        form_layout.addWidget(self.amount_input)
        form_layout.addWidget(self.add_button)
        layout.addLayout(form_layout)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Deskripsi", "Kategori", "Jumlah (Rp)"])
        layout.addWidget(self.table)

        # Label Total
        self.total_label = QLabel("Total Pengeluaran: Rp 0")
        self.total_label.setStyleSheet("font-size: 14px; font-weight: bold; color: darkred;")
        layout.addWidget(self.total_label)

        # Menu
        menu_bar = QMenuBar()
        file_menu = QMenu("File", self)
        about_action = file_menu.addAction("Tentang Aplikasi")
        about_action.triggered.connect(self.show_about)
        menu_bar.addMenu(file_menu)
        layout.setMenuBar(menu_bar)

        self.setLayout(layout)

    def add_expense(self):
        desc = self.desc_input.text()
        category = self.category_input.currentText()
        amount = self.amount_input.value()

        if desc == "" or amount == 0:
            QMessageBox.warning(self, "Input Error", "Isi deskripsi dan jumlah dengan benar.")
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(desc))
        self.table.setItem(row, 1, QTableWidgetItem(category))
        self.table.setItem(row, 2, QTableWidgetItem(f"{amount}"))

        self.desc_input.clear()
        self.amount_input.setValue(0)

        self.update_total()

    def update_total(self):
        total = 0
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 2)
            if item:
                try:
                    total += int(item.text())
                except ValueError:
                    pass  # skip invalid values

        self.total_label.setText(f"Total Pengeluaran: Rp {total}")

    def show_about(self):
        QMessageBox.information(self, "Tentang Aplikasi", "Aplikasi ini dibuat oleh Andi Sibwayiq (F1D022002) untuk mencatat pengeluaran harian.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())


