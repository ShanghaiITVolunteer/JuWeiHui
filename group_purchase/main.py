from pathlib import Path

from community.jia_yi_shui_an import JiaYiShuiAn
from purchase_deliver.parser_mng import get_excel_parser
from utils.utils import *

if __name__ == '__main__':
    # 1. 先指定小区和excel模板，小区用对象（以后这个对象是全局的，生命周期很长），模板用类（模板对象生命周期很短，处理完就销毁了）
    community = JiaYiShuiAn()
    # 2. 指定输入和输出文件名。输入和输出文件名应和需求名有关，输入模板和输出模板会依赖这个。TODO: 其实我觉得不应该依赖，下一步要确认下这个逻辑
    for file in find_all_files("..\\files", ["xlsx"]):
        excel_parser = ExcelParser1 if ("鸡蛋" not in file[1]) and ("清美" not in file[1]) else ExcelParser2
        input_filename = file[0] + '\\' + file[1]
        product_name = Path(input_filename).stem
        output_filename = f'..\\outputs\\{product_name}.pdf'
        print(output_filename)
        # 3. 调用接口处理excel
        # 3.1 创建parser实例，一个parser对应一个excel文件
        parser = excel_parser(open(input_filename, 'rb'))
        # 3.2 调用parser解析接口，返回订单集合对象和出错单元格坐标
        result, errors = parser.parse_for_community(community)
        # 3.3 按需生成pdf或提示用户检查原表格数据
        if errors:
            print('以下单元格数据无法识别，请检查', errors)
        else:
            pass
        result.print_to_pdf(output_filename)
