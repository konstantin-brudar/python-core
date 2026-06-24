import argparse

from utils import Tree


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", nargs="?", default=".", help="directory")
    parser.add_argument("-L", type=int, default=0, help="max level of tree")
    parser.add_argument("-d", action="store_true", help="show directories only")
    args = parser.parse_args()

    directory = args.dir.strip()
    max_level = max(args.L, 0)
    is_dir_mode = args.d

    return directory, max_level, is_dir_mode


if __name__ == "__main__":
    directory, max_level, is_dir_mode = parse_options()
    tree = Tree(directory, is_dir_mode, max_level)
    tree.print()
