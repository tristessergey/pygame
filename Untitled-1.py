from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])
win = QWidget()

text = QTextEdit()
ql = QLabel('Список заметок')
lw = QListWidget()
col1 = QVBoxLayout()
col1.addWidget(text)

col2 = QVBoxLayout()
col2.addWidget(ql)
col2.addWidget(lw)

main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)

win.show()
app.exec_()