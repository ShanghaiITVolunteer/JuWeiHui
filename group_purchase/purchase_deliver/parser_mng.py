from typing import *

from .excel_parser.excel_parser import ExcelParserBase
from .excel_parser.jielong_parser import JieLongParser
from .excel_parser.kuaituantuan_parser import KuaiTuanTuanParser

parser_map: Mapping[str, Type[ExcelParserBase]] = {
    '群接龙': JieLongParser,
    '快团团': KuaiTuanTuanParser
}


def get_excel_parser(name: str) -> Optional[Type[ExcelParserBase]]:
    return parser_map.get(name, None)
