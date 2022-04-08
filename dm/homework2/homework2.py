from typing import List, Set
import json
import matplotlib.pyplot as plt

from .load_data import load_transaction, load_fake_transaction
from dm.fp_tree.fp_tree import FPTree
from dm.fp_tree.transaction import Transactions
from dm.fp_tree.mining import get_frequent_set
from dm.fp_tree.rule import AssociationRule
from dm.common_utils import save_json


def save_rules(rules):
    def f(x):
        return {
            "rule": str(x[0]),
            "support": x[1],
            "confidence": x[2],
            "evaluation": x[3]
        }

    rules = list(map(f, rules))
    save_json(rules, "output/homework2/rules.json")


def calc_support_item_set_and_save(item_sets, t: Transactions):
    result = []
    for item_set in item_sets:
        support = t.calc_support_of_item_set(item_set)
        result.append({
            "itemSet": str(item_set),
            "support": support
        })
    result.sort(key=lambda x: x["support"], reverse=True)
    save_json(result, "output/homework2/frequent_sets.json")


def draw_eval_and_save(rules, eval_name: str):
    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title(eval_name)

    labels = list(map(lambda x: str(x[0]), rules))
    values = list(map(lambda x: x[3][eval_name], rules))

    ax.bar(labels, values)
    ax.set_xticklabels(labels, rotation=45)
    fig.savefig(f"output/homework2/eval_{eval_name}.png")
    # plt.show()


def homework2():
    # transaction = load_fake_transaction()
    transaction = load_transaction()
    # tree = FPTree.from_transactions_unprocessed(transaction, 3)
    # prefix_t = tree.get_prefix("m")
    # print(prefix_t.ts)

    item_set = list(get_frequent_set(transaction, 2000))
    calc_support_item_set_and_save(item_set, transaction)
    # get only 1-itemset
    item_set = list(filter(lambda s: len(s.li) == 1, item_set))
    # print(item_set)
    # print(len(item_set))

    rules = []
    for i in range(len(item_set)):
        for j in range(len(item_set)):
            if i == j:
                continue
            rule = AssociationRule(item_set[i], item_set[j])
            sup = transaction.calc_support_of_association_rule(rule)
            if sup == 0:
                continue
            conf = transaction.calc_confidence_of_association_rule(rule)
            evaluation = transaction.evaluate_rule(rule)
            rules.append((rule, sup, conf, evaluation))
            print(rule, evaluation)

    rules.sort(key=lambda x: x[2], reverse=True)
    save_rules(rules)

    top20_rules = rules[:20]
    draw_eval_and_save(top20_rules, "cosine")
    draw_eval_and_save(top20_rules, "allconf")
    draw_eval_and_save(top20_rules, "lift")
    draw_eval_and_save(top20_rules, "jaccard")
    # print(top10_rules)

    # print(transaction.ts[10])
    # t2, _ = transaction.extract_frequent(500)
    # print(t2.ts[10])
    #
    # tree = FPTree()
    # tree.update_with_transactions(t2)

