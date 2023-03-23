from PyPDF2 import PdfFileWriter, PdfFileReader, PdfWriter, PdfReader
import os

def append_pdf(input, output):
    # [output.addPage(input.getPage(page_num)) \
    #  for page_num in range(input.numPages)]

    [output.add_page(input.pages[page_num]) \
     for page_num in range(len(input.pages))]


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for page in range(144, pdf.getNumPages(), 1):
        if page==152:
            break
        
        pdf_writer.addPage(pdf.getPage(page))

    output_filename = '{}_page_{}.pdf'.format(
        fname, page + 1)
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print('Created: {}'.format(output_filename))


# output = PdfFileWriter()
output = PdfWriter()
dir = 'pdfs/'
#to split pdfs uncomment below
# pdf_splitter(dir+'Orignal.pdf')
#to concatenate pdfs uncomment below
for pdf in filter(lambda x: '.pdf' in x, sorted(os.listdir(dir))):
    print(pdf)
    # reader = PdfFileReader(dir+pdf)
    # for i in range(reader.numPages):
    #     page = reader.getPage(i)
    #     page.compressContentStreams()
    #     output.addPage(page)
    # append_pdf(PdfFileReader(open(dir+pdf, "rb")), output)
    append_pdf(PdfReader(open(dir + pdf, "rb")), output)
output.write(open("final.pdf", "wb"))
