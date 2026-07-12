from benchmark import benchmark
from judge import evaluate


def dummy_generator(video):

    return {
        "formal": "Example formal caption.",
        "sarcastic": "Example sarcastic caption.",
        "humorous-tech": "Example tech joke.",
        "humorous-non-tech": "Example funny caption."
    }


results = benchmark(dummy_generator)

for item in results:

    score = evaluate(
        item["reference"],
        item["prediction"]
    )

    print("=" * 50)

    print(item["video"])

    print(score)