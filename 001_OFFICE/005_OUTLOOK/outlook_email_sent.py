from datetime import date
import datetime
import time
import win32com.client as win32

class Outlook(object):
    def __init__(self,title, mailto, mailcc, textbody):
        self.title = title
        self.mailto = mailto
        self.mailcc = mailcc
        self.textbody = textbody

    def getTitle(self):
        return self.title
    def getMailTo(self):
        return self.mailto
    def getMailCC(self):
        return self.mailcc
    def getBody(self):
        return self.textbody

    def mailContents(self):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        textTitle = self.title
        textMailTo = self.mailto
        textMailCC = self.mailcc
        textBody = self.textbody

        mail.Subject = textTitle
        mail.To = textMailTo
        mail.CC = textMailCC
        mail.GetInspector
        mail.HTMLBody = textBody + mail.HTMLBody
        mail.Display()

def num_1():
    today = str(date.today().strftime("%Y.%m.%d"))
    texttitle = "메일제목(" + today + ")"   # 메일제목(2019.01.10)
    textMailTo = "받는사람"
    textMailCC = "참조"
    textBody = """
      <body>
        <p>안녕하세요...<br>
           <br>
           <br>
           <br>
           감사합니다. <br>
           홍길동 드림
        </p>
      </body>
    """
    _mailinfo = {'title': texttitle, 'mailTo': textMailTo, 'mailCC': textMailCC, 'htmlBody': textBody}
    return _mailinfo
def num_2():
    today = str(date.today().strftime("%Y.%m.%d"))
    texttitle = "메일제목(" + today + ")"   # 메일제목(2019.01.10)
    textMailTo = "받는사람2"
    textMailCC = "참조"
    textBody = """
      <body>
        <p>안녕하세요...<br>
           <br>
           <br>
           <br>
           감사합니다. <br>
           홍길동 드림
        </p>
      </body>
    """
    _mailinfo = {'title': texttitle, 'mailTo': textMailTo, 'mailCC': textMailCC, 'htmlBody': textBody}
    return _mailinfo

menu = """
1. XX에게 메일 보내기

2. XX에게 메일 보내기

3. 미구현...

※ 메뉴 외 번호를 입력하면 
    프로그램이 종료 됩니다...
"""

while True:
    print(menu)
    num = int(input("실행 할 메뉴를 선택하세요."))
    if num == 1:
        print("1번을 선택했습니다.")
        # 메일
        print("실행 중... \n")
        a = Outlook(num_1().get('title'), num_1().get('mailTo'), num_1().get('mailCC'), num_1().get('htmlBody'))
        a.mailContents()
        print("실행 완료... \n")
    elif num == 2:
        print("2번을 선택했습니다.")
        print("실행 중... \n")
        # 메일
        a = Outlook(num_2().get('title'), num_2().get('mailTo'), num_2().get('mailCC'), num_2().get('htmlBody'))
        a.mailContents()
        print("실행 완료... \n")

    else:
        print("종료 합니다.")
        break