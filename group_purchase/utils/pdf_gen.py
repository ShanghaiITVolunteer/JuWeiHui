import pdfkit
import os
import platform

# TODO: 写的有点草率，之后再斟酌下。。。
def html_string_to_pdf(html, filename):
    file = os.path.abspath(__file__)
    src_directory = os.path.dirname(os.path.dirname(file))
    css_file = os.path.join(src_directory, "assets", "html_format.css")

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe') \
        if platform.system() == 'Windows' else None

    pdfkit.from_string(
        html,
        filename,
        configuration=config,
        options={
            'encoding': 'utf-8',
            'footer-center': '第[page]页  共[topage]页'
        },
        css=[css_file])
