def describe_frames(frames):

    description = []

    for frame in frames:
        description.append(
            f"Frame detected: {frame}"
        )

    return "\n".join(description)