import os
from dotenv import load_dotenv


load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "Video Captioning AI"
)


FIREWORKS_API_KEY = os.getenv(
    "FIREWORKS_API_KEY"
)


FIREWORKS_BASE_URL = os.getenv(
    "FIREWORKS_BASE_URL"
)


DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL"
)


MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        512
    )
)


TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        0.2
    )
)