from app.models.fireworks_llm import (
    fireworks_llm
)


def enhance_caption(
    caption: str,
    transcript: str
):

    improved_caption = (
        fireworks_llm
        .improve_caption(
            caption,
            transcript
        )
    )


    return improved_caption