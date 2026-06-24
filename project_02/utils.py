from pathlib import Path


class TreeNode:
    def __init__(self, file):
        self.file = file
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def sort_children(self):
        self.children = sorted(self.children, key=lambda child: child.file.name)


class Tree:
    def __init__(self, directory, is_dir_mode, max_level):
        self.DIRECTORY = directory
        self.IS_DIR_MODE = is_dir_mode
        self.MAX_LEVEL = max_level
        self.directories = 1
        self.files = 0
        self._root = TreeNode(Path(self.DIRECTORY))

        self._add_files(self._root)

    def print(self):
        print(self.DIRECTORY)
        self._print_node(self._root)
        print()
        self.print_stats()

    def print_stats(self):
        dirs = "directories" if self.directories != 1 else "directory"
        files = "files" if self.files != 1 else "file"

        if self.IS_DIR_MODE:
            print(f"{self.directories} {dirs}")
        else:
            print(f"{self.directories} {dirs}, {self.files} {files}")

    def _print_node(self, node, prefix=""):
        for i, child in enumerate(node.children):
            is_last = i == len(node.children) - 1
            corner = "└── " if is_last else "├── "
            print(prefix + corner + child.file.name)

            if child.file.is_dir():
                level = "    " if is_last else "│   "
                next_prefix = prefix + level
                self._print_node(child, next_prefix)

    def _add_files(self, node, level=1):
        if self.MAX_LEVEL and level > self.MAX_LEVEL:
            return

        if not node.file.is_dir():
            return

        for file in node.file.iterdir():
            if self.IS_DIR_MODE and not file.is_dir():
                continue

            child = TreeNode(file)
            node.add_child(child)

            self._update_stats(file)

        node.sort_children()

        for child in node.children:
            self._add_files(child, level + 1)

    def _update_stats(self, file):
        if file.is_dir():
            self.directories += 1
        elif file.is_file():
            self.files += 1
