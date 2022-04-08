from __future__ import annotations
from typing import List, Set, Tuple

from .rule import AssociationRule
from .item_set import ItemSet
from .evaluation import RuleEvaluation


class Transactions:
    def __init__(self):
        self.ts: List[Tuple[List[str], int]] = []
        self.all_items: Set[str] = set()

    # items may not be sorted
    def add(self, items: List[str], dup: int):
        self.ts.append((items, dup))
        for item in items:
            self.all_items.add(item)

    def get_frequent_1_desc(self, support: int) -> List[Tuple[str, int]]:
        count = {}
        for (items, c) in self.ts:
            for item in items:
                if item not in count:
                    count[item] = 0
                count[item] += c

        temp = []
        for key in count:
            temp.append((key, count[key]))
        temp.sort(key=lambda x: x[1], reverse=True)

        temp = filter(lambda x: x[1] >= support, temp)

        return list(temp)

    def get_frequent_1_desc_str(self, support: int) -> List[str]:
        return list(map(lambda x: x[0], self.get_frequent_1_desc(support)))

    # 在绝对support下，提取长度为1的频繁项集并排序，将每个transaction的item都按此排序，剔除不在F-list里的项
    def extract_frequent(self, support: int) -> Tuple[Transactions, List[Tuple[str, int]]]:
        frequent_list = self.get_frequent_1_desc(support)
        # print(frequent_list)

        result = Transactions()
        for (items, count) in self.ts:
            new_items: List[str] = []
            for item, _ in frequent_list:
                if item in items:
                    new_items.append(item)
            if len(new_items) > 0:
                result.add(new_items, count)

        return result, frequent_list

    def calc_support_of_item_set(self, item_set: ItemSet) -> int:
        result = 0
        for (items, count) in self.ts:
            if all([i in items for i in item_set.li]):
                result += count
        return result

    def calc_support_of_association_rule(self, rule: AssociationRule) -> int:
        u = rule.union()
        return self.calc_support_of_item_set(u)

    def calc_confidence_of_association_rule(self, rule: AssociationRule) -> float:
        u = rule.union()
        return self.calc_support_of_item_set(u) / self.calc_support_of_item_set(rule.a)

    def evaluate_rule(self, rule: AssociationRule):
        u = rule.union()
        length = len(self.ts)
        ab = self.calc_support_of_item_set(u) / length
        a = self.calc_support_of_item_set(rule.a) / length
        b = self.calc_support_of_item_set(rule.b) / length
        return {
            "lift": RuleEvaluation.lift(ab, a, b),
            "allconf": RuleEvaluation.allconf(ab, a, b),
            "jaccard": RuleEvaluation.jaccard(ab, a, b),
            "cosine": RuleEvaluation.cosine(ab, a, b)
        }
