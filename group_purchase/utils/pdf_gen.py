import pdfkit
import os

# TODO: 写的有点草率，之后再斟酌下。。。
def html_string_to_pdf(html, filename):
    file = os.path.abspath(__file__)
    src_directory = os.path.join(os.path.pardir, os.path.dirname(file))
    css_file = os.path.join(src_directory, "asserts", "html_format.css")

    pdfkit.from_string(html, filename, options={
        'encoding': 'utf-8',
        'user-style-sheet': css_file,
        'footer-center': '第[page]页  共[topage]页'
    })
