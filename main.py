from PyQt6.QtWidgets import *
import random

import questions
from menu import menu_window

app = QApplication([])
window = QWidget()
window.resize(350, 50)

mainline = QVBoxLayout()
line1 = QHBoxLayout()

ans_box = QGroupBox('Варіанти відповідей')
group_line = QVBoxLayout()
group_h_line = QHBoxLayout()
group_h_line2 = QHBoxLayout()

ans1 = QRadioButton()
ans2 = QRadioButton()
ans3 = QRadioButton()
ans4 = QRadioButton()
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
quest_lbl = QLabel()


line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(rest_btn)
line1.addWidget(rest_time)
line1.addWidget(rest_text)

mainline.addLayout(line1)
mainline.addWidget(quest_lbl)

mainline.addWidget(ans_box)
mainline.addWidget(answer_btn)
mainline.addWidget(next_btn)

answers = [ans1, ans2, ans3, ans4]
def set_quest():
    try:
        random.shuffle(answers)
        quest = questions.questions[questions.counter]
        quest_lbl.setText(quest["Запитання"])
        answers[0].setText(quest['Правильна відповідь'])
        answers[1].setText(quest['Неправильна відповідь'])
        answers[2].setText(quest['Неправильна відповідь1'])
        answers[3].setText(quest['Неправильна відповідь2'])
    except:
        print('Більше запитань немає')
def ans_func():
    for answer in answers:
        answer.hide()
    answer_btn.hide()
    result_lbl.show()
    next_btn.show()
    if answers[0].isChecked():
        result_lbl.setText("Правильно!")

def next_quest():
    questions.counter += 1
    set_quest()
    next_btn.hide()
    answer_btn.show()

    for answer in answers:
        answer.show()

answer_btn.clicked.connect(ans_func)
next_btn.clicked.connect(next_quest)
menu_btn.clicked.connect(menu_window)

set_quest()

window.setLayout(mainline)
window.show()
app.exec()