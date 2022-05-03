
from group_purchase.community.parser_mng import get_community_parser
from group_purchase.purchase_deliver.parser_mng import get_excel_parser

import openpyxl

def on_file(input_file_path, output_file_path, community, excel):
    excel_parser = get_excel_parser(excel)
    community_parser = get_community_parser(community)

    parser = excel_parser(open(input_file_path, 'rb'))
    result, errors = parser.parse_for_community(community_parser())
    if errors:
        return False, f"以下单元格数据无法识别，请检查:\n{errors}"
    else:
        pass

    result.print_to_pdf(output_file_path)
    return True, output_file_path


def update_file(input_file_path, updated_data, coordinate):
    try:
        workbook = openpyxl.load_workbook(open(input_file_path, 'rb'))
        sheet = workbook.active
        sheet[coordinate].value = updated_data
        workbook.save(input_file_path)
        return True, input_file_path
    except Exception as error:
        error_msg = f"Cannot modify file {input_file_path}, error:\n {error}"
        print(error_msg)
        return False, error_msg

