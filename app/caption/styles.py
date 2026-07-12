from enum import Enum


class CaptionStyle(str, Enum):
    FORMAL = "formal"
    SARCASTIC = "sarcastic"
    HUMOR_TECH = "humorous-tech"
    HUMOR = "humorous-non-tech"