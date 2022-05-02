from typing import *

from .community_base import CommunityBase
from .jia_yi_shui_an import JiaYiShuiAn

parser_map: Mapping[str, Type[CommunityBase]] = {
    '嘉怡水岸': JiaYiShuiAn,
}


def get_community_parser(name: str) -> Optional[Type[CommunityBase]]:
    return parser_map.get(name, None)
