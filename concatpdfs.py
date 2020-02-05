from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) \
     for page_num in range(input.numPages)]


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            fname, page + 1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))


output = PdfFileWriter()
dir = 'pdfs/'
# pdf_splitter(dir+'Orignal.pdf')
for pdf in filter(lambda x: '.pdf' in x, sorted(os.listdir(dir))):
    print(pdf)
    # reader = PdfFileReader(dir+pdf)
    # for i in range(reader.numPages):
    #     page = reader.getPage(i)
    #     page.compressContentStreams()
    #     output.addPage(page)
    append_pdf(PdfFileReader(open(dir+pdf, "rb")), output)

output.write(open("final.pdf", "wb"))