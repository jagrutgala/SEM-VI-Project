from PyQt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
import sys, requests

class QuestionLayout:
    def __init__(self, question) -> None:
        self.question = question
        self.initGUI()

    def initGUI(self):
        self.widget = qtw.QWidget()
        self.layout = qtw.QHBoxLayout(self.widget)
        self.question_label = qtw.QLabel(text="(Q) " + str(self.question.get("question_string")))
        self.question_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.answer_label = qtw.QLabel(text="(Ans) " + str(self.question.get("answer")))
        self.answer_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.answer_label.setVisible(False)

        self.answer_btn = qtw.QPushButton(text="Answer")
        self.copy_btn = qtw.QPushButton(text="Copy")
        self.widget.setStyleSheet('font-family: "Arial"; font-size: 24px; border-bottom: 2px solid #a8a3a3')
        self.answer_label.setFont(qtg.QFont("Arial", 24, 200, False))

        self.layout.addWidget(self.question_label, 1)
        self.layout.addWidget(self.answer_label, 1)
        self.layout.addWidget(self.answer_btn, alignment=qtc.Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.copy_btn, alignment=qtc.Qt.AlignmentFlag.AlignRight)

        self.answer_btn.clicked.connect(lambda: self.showAnwer())
        self.copy_btn.clicked.connect(lambda: self.copy())

    def showAnwer(self):
        self.answer_label.setVisible(not self.answer_label.isVisible())

    def copy(self):
        qtw.QApplication.clipboard().setText(str(self.question_label.text()))

class AnswerList:
    def __init__(self, mainWidget) -> None:
        self.mainWidget = mainWidget
        self.initGUI()

    def initGUI(self):
        self.scroll = qtw.QScrollArea()
        self.group_widget = qtw.QWidget()
        self.layout = qtw.QVBoxLayout(self.group_widget)
        self.layout.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.group_widget)
        self.scroll.setMinimumWidth(500)
        self.scroll.setMinimumHeight(400)

        # [self.layout.addWidget(qtw.QPushButton(f"Button{_}")) for _ in range(10)]

    def add(self, widget):
        self.layout.addWidget(widget)

    def removeAll(self):
        for c in range(self.layout.count()):
            self.layout.itemAt(c).widget().deleteLater()


class SideBarLayout:
    def __init__(self, mainWidget, list_:AnswerList) -> None:
        self.mainWidget = mainWidget
        self.initGUI()
        self.listWidget = list_

    def initGUI(self):
        self.layout = qtw.QVBoxLayout()

        self.row_layouts =[]

        row1 = qtw.QHBoxLayout()
        self.topic_label = qtw.QLabel(text="Topic: ")
        self.topic_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.topic_combobox = qtw.QComboBox()
        self.topic_combobox.addItems(list(map(str, requests.get(f"http://127.0.0.1:5000/available topics").json())))
        self.topic_combobox.setCurrentText("")
        row1.addWidget(self.topic_label)
        row1.addWidget(self.topic_combobox)
        self.row_layouts.append(row1)

        row2 = qtw.QHBoxLayout()
        self.type_label = qtw.QLabel(text="Type: ")
        self.type_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.type_combobox = qtw.QComboBox()
        self.type_combobox.addItems(list(map(str, requests.get(f"http://127.0.0.1:5000/available types", params={f"topic":{str(self.topic_combobox.currentText())}}).json())))
        row2.addWidget(self.type_label)
        row2.addWidget(self.type_combobox)
        self.row_layouts.append(row2)

        row3 = qtw.QHBoxLayout()
        self.noq_label = qtw.QLabel(text="No of Questions: ")
        self.noq_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.noq_spinbox = qtw.QSpinBox()
        self.noq_spinbox.setMinimum(1)
        self.noq_spinbox.setMaximum(1000)
        row3.addWidget(self.noq_label)
        row3.addWidget(self.noq_spinbox)
        self.row_layouts.append(row3)

        row4 = qtw.QHBoxLayout()
        self.ll_label = qtw.QLabel(text="Lower Limit: ")
        self.ll_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.ll_spinbox = qtw.QSpinBox()
        self.ll_spinbox.setMinimum(1)
        self.ll_spinbox.setMaximum(1000)
        row4.addWidget(self.ll_label)
        row4.addWidget(self.ll_spinbox)
        self.row_layouts.append(row4)
        
        row5 = qtw.QHBoxLayout()
        self.ul_label = qtw.QLabel(text="Upper Limit: ")
        self.ul_label.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.ul_spinbox = qtw.QSpinBox()
        self.ul_spinbox.setMinimum(2)
        self.ul_spinbox.setMaximum(1000)
        row5.addWidget(self.ul_label)
        row5.addWidget(self.ul_spinbox)
        self.row_layouts.append(row5)

        row6 = qtw.QHBoxLayout()
        self.generate_btn = qtw.QPushButton("Generate")
        self.reset_btn = qtw.QPushButton(self.mainWidget, text="Reset")
        row6.addWidget(self.generate_btn)
        row6.addWidget(self.reset_btn)
        self.row_layouts.append(row6)
        
        row7 = qtw.QHBoxLayout()
        self.clear_answer_btn = qtw.QPushButton("Clear")
        row7.addWidget(self.clear_answer_btn)
        self.row_layouts.append(row7)
        
        for r in self.row_layouts:
            self.layout.addLayout(r)
        
        for l in range(self.layout.count()):
            self.layout.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        self.topic_combobox.currentTextChanged.connect(lambda: self.getTypes(str(self.topic_combobox.currentText())))
        self.generate_btn.clicked.connect(lambda :self.generateQestions())
        self.reset_btn.clicked.connect(lambda :self.clearForm())
        self.clear_answer_btn.clicked.connect(lambda :self.listWidget.removeAll())

    # @qtc.pyqtSlot()
    def generateQestions(self):
        topic_ = self.topic_combobox.currentText()
        type_ = self.type_combobox.currentText()
        noq_ = self.noq_spinbox.value()
        ll_ = self.ll_spinbox.value()
        ul_ = self.ul_spinbox.value()

        # pre checks 
        if ll_ > ul_:
            self.limitError()
            return
        # call question_request
        question_options ={"q_topic": topic_,"q_type": type_,"noq": noq_,"ll": ll_,"ul": ul_}
        question_list = self.question_request(question_options)

        if question_list == False:
            qtw.QMessageBox.critical(self.mainWidget, "Error", "Something Went Wrong!", qtw.QMessageBox.Ok, qtw.QMessageBox.Ok)
            return

        # display answer
        if not question_list: return
        for q in question_list:
            self.listWidget.add(QuestionLayout(q).widget)

    # @qtc.pyqtSlot()
    def clearForm(self):
        self.topic_combobox.setCurrentIndex(0)
        self.type_combobox.setCurrentIndex(0)
        self.noq_spinbox.setValue(self.noq_spinbox.minimum())
        self.ll_spinbox.setValue(self.ll_spinbox.minimum())
        self.ul_spinbox.setValue(self.ul_spinbox.minimum())

    def question_request(self, question_options:dict):
        response_data = requests.get(f"http://127.0.0.1:5000/question", json=question_options)
        # response_data = requests.get(f"http://127.0.0.1:5000/question", params=question_options)
        if not response_data.ok:
            return False
        return response_data.json()


    def getTypes(self, topic):
        self.type_combobox.clear()
        self.type_combobox.addItems(list(map(str, requests.get(f"http://127.0.0.1:5000/available types", params={f"topic":{topic}}).json())))

    def limitError(self):
        qtw.QMessageBox.critical(self.mainWidget, "Error", "Lower Limit must be smaller than Upper Limit", qtw.QMessageBox.Ok, qtw.QMessageBox.Ok)

class MainWindow:

    def __init__(self):
        self.initUI()

    def initUI(self):
        self.widget = qtw.QWidget()
        self.widget.setStyleSheet('font-family: "Arial"; font-size: 24px;')
        self.layout = qtw.QHBoxLayout()
        ans_list = AnswerList(self.widget)
        sidebar = SideBarLayout(self.widget, ans_list)
        self.layout.addLayout(sidebar.layout, 0)
        self.layout.addWidget(ans_list.scroll, 1)

        self.widget.setLayout(self.layout)
        self.widget.setWindowTitle('Math Question Generator')
        self.widget.setLayout(self.layout)
        self.widget.show()

def main():
    app = qtw.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()