from pylatex import Document, Section, Subsection, Command, Package, Figure, Tabular
from pylatex.utils import italic, NoEscape
import os

def generate_doc_header():
    geometry_options = {"tmargin":"1.5cm", "lmargin":"1.5cm"}
    doc = Document(geometry_options=geometry_options, default_filepath='basic', documentclass='article')
    doc.packages.add(Package('ctex'))
    doc.append(NoEscape(r'\renewcommand\arraystretch{1.2}'))
    doc.packages.add(Package('ctex'))
    return doc


def generate_table(doc, name, group, title):
    c = 0
    with doc.create(Section(name + ', 共' + str(int(sum(group['订购数量']))) + '单' + title, False)):
        with doc.create(Tabular('|c|c|c|c|c|c|')) as table:
            table.add_hline()
            table.add_row(('需求概述', '业主姓名', '楼栋号', '门牌号', '套餐数量', '配送完成'))
            table.add_hline()
            group.sort_values(by='门牌号', ascending=True)
            for i, ask in group.iterrows():
                table.add_row((f'{name}{int(ask["门牌号"])}号：{title}', ask['收货人'], name, ask['门牌号'], ask['订购数量'], ''))
                table.add_hline()
                c += ask['订购数量']
    return c

def generate_latex(groups, folder, title):
    doc = generate_doc_header()
    c = 0

    for name, group in groups:
        c += generate_table(doc, name, group, title)

    doc.generate_pdf(filepath=os.path.join(folder, title), compiler='xelatex', clean_tex=False)
    tex = doc.dumps()
    print(title, '-', c)