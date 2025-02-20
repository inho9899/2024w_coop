from flask import Flask, request, jsonify, send_file
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
import os

app = Flask(__name__)

# ✅ 텍스트 생성 (기존 LLM 모델)
llm = pipeline("text-generation", model="distilgpt2")

# ✅ 이미지 생성 모델 (Stable Diffusion)
device = "cuda" if torch.cuda.is_available() else "cpu"
sd_model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

@app.route("/generate_text", methods=["POST"])
def generate_text():
    """ 텍스트 생성 API """
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = llm(prompt, max_length=100, num_return_sequences=1)
    return jsonify({"generated_text": response[0]["generated_text"]})

@app.route("/generate_image", methods=["POST"])
def generate_image():
    """ 이미지 생성 API """
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # 이미지 생성
    image = sd_model(prompt).images[0]
    
    # 저장할 경로 설정
    image_path = "generated_image.png"
    image.save(image_path)

    return send_file(image_path, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
