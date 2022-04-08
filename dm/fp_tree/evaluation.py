import math


class RuleEvaluation:
    @staticmethod
    def lift(ab, a, b) -> float:
        return ab / (a * b)

    @staticmethod
    def allconf(ab, a, b) -> float:
        return ab / max(a, b)

    @staticmethod
    def jaccard(ab, a, b) -> float:
        return ab / (a + b - ab)

    @staticmethod
    def cosine(ab, a, b) -> float:
        return ab / math.sqrt(a * b)
