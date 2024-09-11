import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Streamlit 웹앱 제목 설정
st.title("QR Code Generator")

# 사용자로부터 QR 코드에 담을 데이터 입력받기
qr_data = st.text_input("Enter the text or URL to generate QR code:")

# QR 코드를 생성하는 버튼
if st.button("Generate QR Code"):
    if qr_data:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # QR 코드를 이미지로 변환
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.convert('RGB')

        # 이미지 표시
        st.image(img)

        # 이미지 다운로드 버튼 추가
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some data to generate a QR code")
