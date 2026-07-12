from enum import Enum


class CaptionStyle(str, Enum):
    FORMAL = "formal"
    SARCASTIC = "sarcastic"
    HUMOR_TECH = "humorous-tech"
    HUMOR_NON_TECH = "humorous-non-tech"


SUPPORTED_STYLES = [
    CaptionStyle.FORMAL,
    CaptionStyle.SARCASTIC,
    CaptionStyle.HUMOR_TECH,
    CaptionStyle.HUMOR_NON_TECH,
]