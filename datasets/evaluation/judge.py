from difflib import SequenceMatcher


def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


def evaluate(reference, prediction):

    scores = {}

    total = 0

    for style in reference:

        score = similarity(
            reference[style],
            prediction.get(style, "")
        )

        scores[style] = round(score, 3)

        total += score

    scores["average"] = round(
        total / len(reference),
        3
    )

    return scores