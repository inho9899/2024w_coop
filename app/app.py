import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("🖼 AI 기반 이미지 생성기")

# 사용자 입력 받기
user_input = st.text_input("텍스트 입력 (이미지 생성 또는 텍스트 변환):")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 텍스트 생성"):
        if user_input:
            response = requests.post("http://localhost:5000/generate_text", json={"prompt": user_input})
            if response.status_code == 200:
                generated_text = response.json().get("generated_text", "생성 실패")
                st.write("💡 **생성된 텍스트:**")
                st.success(generated_text)
            else:
                st.error("서버 오류 발생!")
        else:
            st.warning("텍스트를 입력하세요!")

with col2:
    if st.button("🎨 이미지 생성"):
        if user_input:
            response = requests.post("http://localhost:5000/generate_image", json={"prompt": user_input})
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="🖼 생성된 이미지", use_column_width=True)
            else:
                st.error("이미지 생성 오류 발생!")
        else:
            st.warning("텍스트를 입력하세요!")
