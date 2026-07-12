from app.fireworks.client import FireworksClient
from app.caption.prompts import build_prompt
from app.caption.styles import CaptionStyle

client = FireworksClient()


def generate_captions(transcript: str, visual_description: str):
    """
    Generate captions in all four required styles.
    """

    captions = {}

    for style in CaptionStyle:
        prompt = build_prompt(
            transcript,
            visual_description,
            style
        )

        result = client.generate(
            model="accounts/fireworks/models/llama4-maverick-instruct-basic",
            prompt=prompt
        )

        if isinstance(result, dict) and result.get("error"):
            captions[style.value] = result
        else:
            captions[style.value] = result

    return captions