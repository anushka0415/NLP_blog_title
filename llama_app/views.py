from django.http import JsonResponse
from transformers import pipeline,AutoTokenizer, AutoModelForCausalLM
import json
from django.views.decorators.csrf import csrf_exempt
import os
import torch
from huggingface_hub import login
from config import HF_TOKEN  

# Load LLaMA model and tokenizer (this may take time)
model_name = "meta-llama/Llama-3.2-1B-Instruct"

login(token = HF_TOKEN)
pipe = pipeline(
    "text-generation",
    model=model_name,
    torch_dtype=torch.bfloat16,
    device_map="cpu",
)

# Directory to save JSON files
SAVE_DIR = "generated_titles"
os.makedirs(SAVE_DIR, exist_ok=True)
@csrf_exempt
def generate_text(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        text = body.get("text", "")

        if not text:
            return JsonResponse({"error": "No text provided"}, status=400)
        
        messages = [
    {"role": "system", "content": f"you need to provide creative title for {text}.just return the title.don't add any comments anything."},
]
        
        outputs = pipe(
            messages,
            max_new_tokens=256,
        )
        title_=outputs[0]["generated_text"][-1]
        title=title_["content"]

        response_data = {"text": text, "title": title}

        filename = os.path.join(SAVE_DIR, f"title_{len(os.listdir(SAVE_DIR)) + 1}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=4)

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)


