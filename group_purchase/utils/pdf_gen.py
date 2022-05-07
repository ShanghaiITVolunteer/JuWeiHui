import pdfkit

# TODO: 写的有点草率，之后再斟酌下。。。
def html_string_to_pdf(html, filename):

    pdfkit.from_string(html, filename, options={
        'encoding': 'utf-8',
        'user-style-sheet': 'group_purchase/assets/html_format.css',
        'footer-center': '第[page]页  共[topage]页'
    })
