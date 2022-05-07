import login
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pymysql
#打开数据库连接
import random

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
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="test", charset="utf8")
        sql = "select * from test.new_table"
        cur = conn.cursor()
        cur.execute(sql)  # 执行sql语句
        data = cur.fetchall()

        username = loginUi.lineEdit.text()   #获取用户登录信息
        password = loginUi.lineEdit_2.text()

        for datas in data:
            if username == datas[1]:
                if password == datas[2]:
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

        cur.close()
        conn.close()
    def sign_up():
        conn = pymysql.connect(host='localhost',
                               user='root',
                               passwd='123456',
                               port=3306,
                               db='test1',
                               charset='utf8')
        cur = conn.cursor()
        sqs = 0
        user = loginUi.lineEdit_3.text()
        password = loginUi.lineEdit_4.text()
        password1 = loginUi.lineEdit_5.text()
        if password != password1:
            loginUi.widget_4.show()
            loginUi.label_5.setText('密码有误')
            sqs += 1
        else:
            conn = pymysql.connect(host="localhost", user="root", password="123456", database="test", charset="utf8")
            sql = "select * from test.new_table"
            cur = conn.cursor()
            cur.execute(sql)  # 执行sql语句
            data = cur.fetchall()
            for datas in data:
                if user == datas[1]:
                    loginUi.widget_4.show()
                    loginUi.label_5.setText('用户已有')
                    sqs += 1
                    break

        if sqs == 0:
            a = random.randint(5,1000)
            sql = f"INSERT INTO `test`.`new_table` (`id`, `username`, `password`) VALUES ('{a}', '{user}', '{password1}');"
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            loginUi.widget_4.show()
            loginUi.label_5.setText('注册成功')
            loginUi.lineEdit_3.setText('')
            loginUi.lineEdit_4.setText('')
            loginUi.lineEdit_5.setText('')

        cur.close()
        conn.close()
    def messgae():
        loginUi.widget_4.hide()
    loginUi.pushButton.clicked.connect(change_widget_2)
    loginUi.pushButton_2.clicked.connect(change_widget_3)
    loginUi.pushButton_3.clicked.connect(sign_in)
    loginUi.pushButton_6.clicked.connect(messgae)
    loginUi.pushButton_5.clicked.connect(sign_up)
    win.show()
    sys.exit(app.exec_())