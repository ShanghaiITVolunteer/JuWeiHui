# JuWeiHui

Currently a very ugly but usable script to covert group purchase results to printable sheets for delivery during the
pandemic in Shanghai

## How to use

1. Define your own personal community logic in the community_hardcode folder. Import this class in main.py and change
   the class name.
2. Create 2 folders files and outputfiles.
3. Put all the files you what to generate in files folder.
4. Run main.py
5. If your file has some missind data, an error will be thrown. Ask the one with missing data to fill the data here.
6. The latex pdf file will be generated in outputfiles folder

## Other points

This repo is more like a hardcode repo to solve temporary problems of the JuWeiHui package delivery. We might have more
types of excel templates, more communities involved. So it will be appreciate if you can help me to make it less
hardcode, and more applicable for more situations.

Users of this form might touch personal data of the purchaser. For me I will delete all those data when the pandemic is
done, and won't send any such data to anyone else. Please make similar declairation if you need to use this script.

I would like to add some algorithm-based features to even improve the delivery logic. If you are a specialist in
optimization, please contact me. Wechat id:wgzjack0305

---

# 订单excel处理方法

1. 先指定小区和excel模板，小区用对象（以后这个对象是全局的，生命周期很长），模板用类（模板对象生命周期很短，处理完就销毁了）
2. 指定输入和输出文件名。输入和输出文件名应和需求名有关，输入模板和输出模板会依赖这个。
3. 调用接口处理excel
    1. 创建parser实例，一个parser对应一个excel文件
    2. 调用parser解析接口，返回订单集合对象和出错单元格坐标
    3. 按需生成pdf或提示用户检查原表格数据

获取excel模板接口：`get_excel_parser(name: str) -> Optional[Type[ExcelParserBase]]`

- 输入：`name`模板的中文名。
- 输出：模板的Parser类。找不到该名称对应的模板时返回None。
- 当前支持模板：
    - 群接龙
    - 快团团
