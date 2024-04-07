from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGroupBox, QLabel, QPushButton, QRadioButton,
    QHBoxLayout, QVBoxLayout, QButtonGroup, 
)

from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Сколько будет 4*3=?', '12', '15', '4', '0'))
question_list.append(Question('Сколько будет 5*3=?', '15', '20', '3', '5'))
question_list.append(Question('Сколько будет 20*4=?', '80', '100', '50', '40'))

app = QApplication([])
wind = QWidget()
wind.setWindowTitle('Memoy Card')
wind.resize(600, 600)

question = QLabel('Сколько будет 4*3=?')
btn_ok = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('12')
rbtn_2 = QRadioButton('15')
rbtn_3 = QRadioButton('4')
rbtn_4 = QRadioButton('0')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Corerect = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Corerect, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)




layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

wind.setLayout(layout_card)


#функции
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


#def start_test():
    #if 'Ответить' == btn_ok.text():
        #show_result()
    #else:
        #show_question()


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Corerect.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        wind.score += 1
        print('Статистика\n-Всего вопросов: ', wind.total, '\n-Правильных ответов: ', wind.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')            
            print('Рейтинг: ', (wind.score/wind.total*100), '%')

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    wind.total += 1
    print('Статистика\n-Всего вопросов: ', wind.total, '\n-Правильных ответов: ', wind.score)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()





btn_ok.clicked.connect(click_OK)
wind.score = 0
wind.total = 0
next_question()

wind.show()
app.exec_()