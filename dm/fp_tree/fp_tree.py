from __future__ import annotations
from typing import List, Optional

from .transaction import Transactions


class FPTreeNode:
    def __init__(self):
        self.children: List[FPTreeNode] = []
        self.count: int = 0
        self.parent: Optional[FPTreeNode] = None
        self.next: Optional[FPTreeNode] = None
        self.name: str = ""

    def get_children(self, name: str) -> Optional[FPTreeNode]:
        for item in self.children:
            if item.name == name:
                return item
        return None

    def add_child(self, node: FPTreeNode):
        self.children.append(node)


class FPTree:
    def __init__(self):
        self.headers: List[FPTreeNode] = []
        self.header_index_map = {}
        self.root = FPTreeNode()
        self.tails = {}

    @staticmethod
    def from_transactions_unprocessed(t: Transactions, support: int) -> FPTree:
        processed, frequent_list = t.extract_frequent(support)
        tree = FPTree()
        # print(frequent_list)

        # add header
        for freq_item, count in frequent_list:
            tree.add_header(freq_item, count)
        tree.finish_add_header()
        tree.update_with_transactions(processed)

        return tree

    def is_empty(self) -> bool:
        return len(self.headers) == 0

    def get_prefix(self, name: str):
        head_index = self.header_index_map[name]
        head_node = self.headers[head_index]
        node = head_node

        result = Transactions()
        while node.next is not None:
            path = []
            n = node.next.parent
            while n is not self.root:
                path.append(n.name)
                n = n.parent
            path.reverse()
            result.add(path, node.next.count)

            node = node.next
        return result

    def add_header(self, name: str, count: int):
        node = FPTreeNode()
        node.count = count
        node.name = name

        self.tails[name] = node
        self.headers.append(node)

    def finish_add_header(self):
        self.headers.sort(key=lambda x: x.count, reverse=True)
        for (index, item) in enumerate(self.headers):
            item: FPTreeNode
            self.header_index_map[item.name] = index

    def get_header_node(self, name: str) -> FPTreeNode:
        index = self.header_index_map[name]
        return self.headers[index]

    # li is sorted by count, but count in omitted
    def update_with_list(self, li: List[str], count: int):
        node = self.root
        for name in li:
            child = node.get_children(name)
            if child is None:
                # branch
                new_node = FPTreeNode()
                new_node.count = count
                new_node.parent = node
                new_node.name = name

                tail: FPTreeNode = self.tails[name]
                tail.next = new_node
                node.add_child(new_node)

                self.tails[name] = new_node
                child = new_node
            else:
                child.count += count

            node = child

    def update_with_transactions(self, t: Transactions):
        for (items, count) in t.ts:
            self.update_with_list(items, count)
