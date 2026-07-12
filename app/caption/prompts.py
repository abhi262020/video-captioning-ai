from app.caption.styles import CaptionStyle


def build_prompt(transcript: str, visual_description: str, style: CaptionStyle):

    styles = {
        CaptionStyle.FORMAL:
            "Write a professional caption summarizing the video.",

        CaptionStyle.SARCASTIC:
            "Write a sarcastic caption that is funny but not offensive.",

        CaptionStyle.HUMOR_TECH:
            "Write a humorous caption using programming or AI jokes.",

        CaptionStyle.HUMOR:
            "Write a funny caption suitable for social media."
    }

    return f"""
Video Transcript:
{transcript}

Visual Description:
{visual_description}

Instruction:
{styles[style]}

Return only the caption.
"""