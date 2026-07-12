from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch


class CLIPFeatureExtractor:

    def __init__(self):
        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    def extract_features(self, image_path: str):

        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        with torch.no_grad():
            features = self.model.get_image_features(**inputs)

        return features


clip_model = CLIPFeatureExtractor()