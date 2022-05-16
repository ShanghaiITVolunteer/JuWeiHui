from typing import *

from group_purchase.community.qing_shui_yuan import QingShuiYuan

from .community_base import CommunityBase
from .jia_yi_shui_an import JiaYiShuiAn

parser_map: Mapping[str, Type[CommunityBase]] = {
    '嘉怡水岸': JiaYiShuiAn,
    '清水苑': QingShuiYuan,
}


def get_community_parser(name: str) -> Optional[Type[CommunityBase]]:
    return parser_map.get(name, None)
