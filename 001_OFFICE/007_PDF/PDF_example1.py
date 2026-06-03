# pip install tika

from tika import parser
print("텍스트 파일을 추출할 PDF파일명을 입력하세요.")
#PDFfileName = input()
PDFfileName = '1.pdf'

print("텍스트 파일을 다음 폴더에 저장됩니다.")
print("./")
inputpath = PDFfileName

parsed = parser.from_file(PDFfileName)
print(parsed["content"])
fileOut = open('fileOut.txt','w', encoding='utf-8')
print(parsed['content'], file=fileOut)
fileOut.close()
