import login
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    loginUi = login.Ui_MainWindow()
    loginUi.setupUi(win)
    loginUi.widget_3.hide()
    loginUi.widget_4.hide()


    def change_widget_3():
        loginUi.widget_2.hide()
        loginUi.widget_3.show()


    def change_widget_2():
        loginUi.widget_3.hide()
        loginUi.widget_2.show()


    def sign_in():
        username = loginUi.lineEdit.text()   #获取用户登录信息
        password = loginUi.lineEdit_2.text()
        with open('user.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                line = line.rsplit()
                if username == line[0]:
                    if password == line[1]:
                        loginUi.widget_4.show()
                        loginUi.label_5.setText('登录成功')
                        loginUi.lineEdit.setText('')
                        loginUi.lineEdit_2.setText('')
                        break
                    else:
                        loginUi.widget_4.show()
                        loginUi.label_5.setText('登陆失败')
                else:
                    loginUi.widget_4.show()
                    loginUi.label_5.setText('登陆失败')
        #print(password)
        #print(username)


    def sign_up():
        sqs = 0
        user = loginUi.lineEdit_3.text()
        password = loginUi.lineEdit_4.text()
        password1 = loginUi.lineEdit_5.text()
        if password != password1:
            loginUi.widget_4.show()
            loginUi.label_5.setText('密码有误')
            sqs +=1
        else:
            with open('user.txt', 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    line = line.rsplit()

                    if user == line[0]:
                        loginUi.widget_4.show()
                        loginUi.label_5.setText('用户已有')
                        sqs += 1
        if sqs == 0:
            with open('user.txt', 'a+', encoding='utf-8') as f:
                f.write('\n' + user + ' ' + password1)
            loginUi.widget_4.show()
            loginUi.label_5.setText('注册成功')
            loginUi.lineEdit_3.setText('')
            loginUi.lineEdit_4.setText('')
            loginUi.lineEdit_5.setText('')


    def messgae():
        loginUi.widget_4.hide()
    loginUi.pushButton.clicked.connect(change_widget_2)
    loginUi.pushButton_2.clicked.connect(change_widget_3)
    loginUi.pushButton_3.clicked.connect(sign_in)
    loginUi.pushButton_6.clicked.connect(messgae)
    loginUi.pushButton_5.clicked.connect(sign_up)
    win.show()
    sys.exit(app.exec_())