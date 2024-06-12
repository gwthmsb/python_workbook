import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

import pathlib
from icecream import ic


def create_watermak(watermark_file):
    # create text watermark with customizable transparency
    pdf = canvas.Canvas(watermark_file, pagesize=A4)
    pdf.translate(inch,
                  inch)  # move the current origin point of the canvas by the given horizontal and vertical distances
    pdf.setFillColor(colors.red,
                     alpha=0.3)  # input the color value and use the alpha value to adjust the transparency of watermark
    pdf.setFont("Helvetica", 30)  # input the font and fo   nt size
    pdf.rotate(45)  # we can rotate the canvas by 45 degrees if needed
    pdf.drawCentredString(400, 300, "THIS DOCUMENT IS ")
    pdf.drawCentredString(400, 225, "FOR THE IMMOBILIER")
    pdf.drawCentredString(400, 100, "USAGE OF THIS DOCUMENT")
    pdf.drawCentredString(400, 25, "FOR ANYTHING ELSE IS FORBIDDEN.")  # choose the positive you would like to put the watermark
    #pdf.drawCentredString(400, 225, "THIS DOCUMENT IS FOR")
    #pdf.drawCentredString(400, 100, "CAF ADMINISTRATION WORK")

    pdf.save()  # export the watermark


def add_watermark(input_pdf, output_pdf, watermark_text):
    # Create a PDF reader object for the input PDF
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object for the output PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Load the watermark as a PDF
        watermark = PyPDF2.PdfReader(watermark_text)

        # Iterate through each page of the input PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page from the input PDF
            page = pdf_reader.pages[page_num]

            # Merge the page with the watermark
            page.merge_page(watermark.pages[0])

            # Add the merged page to the output PDF
            pdf_writer.add_page(page)

        # Write the output PDF to a new file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

        ic("Watermarked file is : {}".format(output_pdf))


def fetch_files_to_watermark_from_folder(folder_name):
    folder = pathlib.Path(folder_name)
    if folder.is_dir():
        return [file for file in folder.iterdir() if file.is_file()]


def extract_file_name_from_pdf_extension(file_name: pathlib.Path):
    return file_name.name.split(".pdf")[0] if ".pdf" in file_name.name else None


def fetch_output_filepath(base_dir, file_name):
    output_dir = pathlib.Path(base_dir+"/output")
    if not output_dir.exists():
        output_dir.mkdir()
    return str(output_dir.absolute()) + "/{}_watermarked.pdf".format(file_name)

# Example usage
#input_pdf_path = 'D:/scratch/target_pdf.pdf'
#output_pdf_path = 'D:/scratch/target_pdf_with_watermak.pdf'


pdfs_folder = 'D:/scratch/'
files = fetch_files_to_watermark_from_folder(pdfs_folder)
ic(files)
output_files = [fetch_output_filepath(pdfs_folder, extract_file_name_from_pdf_extension(file)) for file in files]
ic(output_files)

watermark_text_path = '{}/watermark/watermark.pdf'.format(pdfs_folder)

create_watermak(watermark_file=watermark_text_path)
for file in files:
    add_watermark(file,
                  fetch_output_filepath(pdfs_folder, extract_file_name_from_pdf_extension(file)),
                  watermark_text_path)
