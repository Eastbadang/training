# pip install pdfminer

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt():
    # pdf 리소스 매니저 객체 생성
    rsrcmgr = PDFResourceManager()
    # 문자열 데이터를 파일처럼 처리하는 stringio -> pdf 파일 내용이 여기 담김
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open("./1.pdf", 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0  # is for all
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                              check_extractable=True):
        interpreter.process_page(page)

    # text에 결과가 담김
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()

    return text

v = convert_pdf_to_txt()
print(v)


