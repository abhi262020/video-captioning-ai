from app.models.blip_model import blip_model


def generate_video_caption(
    frames: list
):

    captions = []


    for frame in frames:

        caption = (
            blip_model
            .generate_caption(frame)
        )

        captions.append(
            caption
        )


    final_caption = (
        " ".join(captions)
    )


    return final_caption