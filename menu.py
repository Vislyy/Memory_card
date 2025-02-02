from PyQt6.QtWidgets import *
import questions

def menu_window():
    menu = QDialog()
    menu.resize(300, 200)

    def leave_back():
        menu.close()

    def add_quest():
        questions.questions.append(
            {
                "Запитання": question.text(),
                "Правильна відповідь": right_ans_form.text(),
                "Неправильна відповідь1": ans.text(),
                "Неправильна відповідь2": ans1.text(),
                "Неправильна відповідь": ans2.text(),

            }
        )
        print('Добавлено')

    quest_lbl = QLabel('Запитання')
    ans_lbl = QLabel('Відповіді')
    right_lbl = QLabel('Правильна відповідь')

    right_ans_form = QLineEdit()
    question = QLineEdit()
    ans = QLineEdit()
    ans1 = QLineEdit()
    ans2 = QLineEdit()
    add_btn = QPushButton('Додати')
    back_btn = QPushButton('Назад')

    mainline = QVBoxLayout()
    h1 = QHBoxLayout()
    h2 = QHBoxLayout()
    h3 = QHBoxLayout()
    h4 = QHBoxLayout()
    h5 = QHBoxLayout()

    h5.addWidget(quest_lbl)
    h5.addWidget(question)

    h1.addWidget(ans_lbl)
    h1.addWidget(ans)

    h2.addWidget(ans_lbl)
    h2.addWidget(ans1)

    h3.addWidget(ans_lbl)
    h3.addWidget(ans2)

    h4.addWidget(right_lbl)
    h4.addWidget(right_ans_form)

    mainline.addLayout(h5)
    mainline.addLayout(h1)
    mainline.addLayout(h2)
    mainline.addLayout(h3)
    mainline.addLayout(h4)

    mainline.addWidget(add_btn)
    mainline.addWidget(back_btn)

    back_btn.clicked.connect(leave_back)
    add_btn.clicked.connect(add_quest)

    menu.setLayout(mainline)
    menu.exec()
