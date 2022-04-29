from Communitiy.JiaYiShuiAn import JiaYiShuiAn
from PurchaseDeliver.ExcelParser1 import ExcelParser1

if __name__ == '__main__':
    # 1. 先指定小区和excel模板，小区用对象（以后这个对象是全局的，生命周期很长），模板用类（模板对象生命周期很短，处理完就销毁了）
    community = JiaYiShuiAn()
    excel_parser = ExcelParser1
    # 2. 指定输入和输出文件名。输入和输出文件名应和需求名有关，输入模板和输出模板会依赖这个。TODO: 其实我觉得不应该依赖，下一步要确认下这个逻辑
    input_filename = 'input.xlsx'
    output_filename = 'out.pdf'
    # 3. 调用接口处理excel
    # 3.1 创建parser实例，一个parser对应一个excel文件
    parser = excel_parser(open(input_filename, 'rb'))
    # 3.2 调用parser解析接口，返回订单集合对象和出错单元格坐标
    result, errors = parser.parse_for_community(community)
    # 3.3 按需生成pdf或提示用户检查原表格数据
    if errors:
        print('以下单元格数据无法识别，请检查', errors)
    else:
        result.print_to_pdf(output_filename)
