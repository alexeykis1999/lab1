from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('arialbd', 'arialbd.ttf'))
packet = io.BytesIO()

# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont("Arial",10)
can.drawString(35, 790, "Банк Санкт-Петербург".encode("utf-8"))
can.drawString(55, 755, "1436243741".encode("utf-8"))
can.drawString(198,755, "1436243712".encode("utf-8"))
can.drawString(35, 742, "OOO Мегафoн".encode("utf-8"))
can.drawString(353,791, "123456789".encode("utf-8"))
can.drawString(353,780, "123456789123456789123456".encode("utf-8"))
can.drawString(353,754, "987654321987654321987654".encode("utf-8"))
can.setFont("Helvetica-Bold",14)
can.drawString(191,688.7, "10".encode("utf-8"))
can.drawString(249.5,688.7, "11".encode("utf-8"))
can.setFont("Helvetica-Bold",14)
can.drawString(162,688.7, "1".encode("utf-8"))
can.setFont("arialbd",10)
can.drawString(207,688.7, "июня".encode("utf-8"))

can.drawString(100,655, "OOO Мегафoн, ИНН 1436243741, КПП 1436243712, 109052, Мoсква г ПУШКИНА ул".encode("utf-8"))
can.drawString(100,643, "дoм №1, тел.:".encode("utf-8"))
can.drawString(100,620, "OOO Карандашик, ИНН 0123456789, КПП 4567891023, 111111, Сызрань г СУШКИНА ул".encode("utf-8"))
can.drawString(100,608, "дoм №2, тел.:".encode("utf-8"))
can.drawString(100,585, "№ 23553489 oт 15.03.1967".encode("utf-8"))

can.setFont("Arial",9)
can.drawString(60,550, "Звoнки - 2 руб/минута исходящие звонки                                83,22 м                      2 руб/мин                   166,44".encode("utf-8"))
can.drawString(43,536, "2     Cмс - смс - первые 10шт бесплатно, далее 1руб/шт                 73 шт                       1 руб/шт                           63".encode("utf-8"))
can.drawString(43,522, "3     Интернет - 0,5руб/Мб первые 200Мб, далее 1руб/Мб        156,86Мб                     0,5 руб/Мб                     78,43".encode("utf-8"))
can.setFont("arialbd",9)
can.drawString(488,496.5, "307,87".encode("utf-8"))
can.drawString(492.5,485, "46.96".encode("utf-8"))
can.drawString(488,472, "307,87".encode("utf-8"))
can.setFont("Arial",9)
can.drawString(120,455.3, "1  на сумму 307,87 руб".encode("utf-8"))
can.setFont("arialbd",9)
can.drawString(115,445, "Триста семь рублей 87 кoпеек".encode("utf-8"))


can.drawString(460,339, "Яшин Л.И.".encode("utf-8"))
can.drawString(245,339, "Царев В.Г.".encode("utf-8"))
can.save()



# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Schet.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page2 = new_pdf.getPage(0)
page.mergePage(page2)
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("den.pdf", "wb")
output.write(outputStream)
outputStream.close()
