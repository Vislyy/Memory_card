from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(350, 50)

mainline = QVBoxLayout()
line1 = QHBoxLayout()

ans_box = QGroupBox('Варіанти відповідей')
group_line = QVBoxLayout()
group_h_line = QHBoxLayout()
group_h_line2 = QHBoxLayout()

ans1 = QRadioButton('Building')
ans2 = QRadioButton('Apple')
ans3 = QRadioButton('Chair')
ans4 = QRadioButton('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
result_lbl = QLabel('Результат')
result_lbl.hide()
next_btn = QPushButton('Наступне запитання')
next_btn.hide()

group_h_line2.addWidget(ans3)
group_h_line.addWidget(ans2)
group_h_line.addWidget(ans4)
group_h_line2.addWidget(ans1)

group_line.addWidget(result_lbl)

group_line.addLayout(group_h_line2)
group_line.addLayout(group_h_line)

ans_box.setLayout(group_line)

#Relax elements
rest_text = QLabel('Хвилин')
rest_time = QSpinBox()
rest_btn = QPushButton('Відпочити')

#Menu button
menu_btn = QPushButton('Меню')
#Quiz Elements
answer_btn = QPushButton('Відповісти')
quest_lbl = QLabel('Яблуко')


line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(rest_btn)
line1.addWidget(rest_time)
line1.addWidget(rest_text)

mainline.addLayout(line1)
mainline.addStretch(1)
mainline.addWidget(quest_lbl)

mainline.addWidget(ans_box)
mainline.addWidget(answer_btn)
mainline.addWidget(next_btn)
window.setLayout(mainline)

window.show()
app.exec()