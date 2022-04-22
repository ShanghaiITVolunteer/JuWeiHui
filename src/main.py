import sys
from utils.chinese import *
from utils.utils import *
from utils.latex import *
from community_related_hardcode.jiayishuian import *

def main():
    files = find_all_files('..\\files', ['.xlsx'])
    community = JiaYiShuiAn()
    for f in files:
        p = os.path.splitext(f[1])[0]
        groups = read_excel(os.path.join(f[0], f[1]), community)
        generate_latex(groups, '..\\outputfiles', p)

if __name__ == "__main__":
    main()