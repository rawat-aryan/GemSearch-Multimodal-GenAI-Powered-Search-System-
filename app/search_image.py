
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModel
# import torch

# model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
# processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# def handle_image_query(file):
#     image = Image.open(file.file).convert("RGB")
#     inputs = processor(images=image, return_tensors="pt")
#     with torch.no_grad():
#         features = model.get_image_features(**inputs)
#     return {"image_embedding": features.tolist()[0][:5]}
import clip
import torch
from PIL import Image
from io import BytesIO

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Sample image caption corpus
image_captions = [
    "A dog playing fetch in the park.",
    "A rocket launching into space.",
    "A person working on a laptop with code.",
    "A city skyline at sunset.",
]
caption_tokens = clip.tokenize(image_captions).to(device)
with torch.no_grad():
    caption_embeddings = model.encode_text(caption_tokens)

async def handle_image_query(file):
    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        image_input = preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            image_features = model.encode_image(image_input)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        caption_embeddings_norm = caption_embeddings / caption_embeddings.norm(dim=-1, keepdim=True)

        similarities = (image_features @ caption_embeddings_norm.T)[0]
        top_k = torch.topk(similarities, k=3)

        results = []
        for idx in top_k.indices:
            results.append({
                "caption": image_captions[idx],
                "score": round(float(similarities[idx]), 4)
            })

        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
