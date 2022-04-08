from .item_set import ItemSet


class AssociationRule:
    def __init__(self, a: ItemSet, b: ItemSet):
        self.a = a
        self.b = b

    def __repr__(self):
        return str(self.a) + "->" + str(self.b)

    def union(self) -> ItemSet:
        return self.a.union(self.b)
