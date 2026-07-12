import json

from pathlib import Path


def load_dataset():

    dataset_path = Path("datasets/evaluation.json")

    with open(dataset_path, "r", encoding="utf-8") as f:
        return json.load(f)


def benchmark(generator):

    dataset = load_dataset()

    results = []

    for item in dataset:

        output = generator(item["video"])

        results.append({
            "video": item["video"],
            "prediction": output,
            "reference": item["reference"]
        })

    return results