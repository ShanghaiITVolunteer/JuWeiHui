# JuWeiHui
Currently a very ugly but usable script to covert group purchase results to printable sheets for delivery during the pandemic in Shanghai

## How to use
1. Define your own personal community logic in the community_hardcode folder. Import this class in main.py and change the class name.
2. Create 2 folders files and outputfiles.
3. Put all the files you what to generate in files folder. 
4. Run main.py
5. If your file has some missind data, an error will be thrown. Ask the one with missing data to fill the data here.
6. The latex pdf file will be generated in outputfiles folder

## Other points

This repo is more like a hardcode repo to solve temporary problems of the JuWeiHui package delivery. We might have more types of excel templates, more communities involved. So it will be appreciate if you can help me to make it less hardcode, and more applicable for more situations.

Users of this form might touch personal data of the purchaser. For me I will delete all those data when the pandemic is done, and won't send any such data to anyone else. Please make similar declairation if you need to use this script.

I would like to add some algorithm-based features to even improve the delivery logic. If you are a specialist in optimization, please contact me. Wechat id:wgzjack0305
