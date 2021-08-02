import streamlit as st

from img_classify import classification
from PIL import Image
from image_ocr import get_text



st.sidebar.header("影像處理 APP")
st.sidebar.button("圖片分類", key = 'classification')
st.sidebar.button("圖片 OCR", key = 'ocr')



# if st.button("classification"):

#     st.title('圖像分類 APP')
#     st.header('圖片分類APP')
#     st.text('請上傳圖片進行影像分類')
    
    
#     uploaded_file = st.file_uploader("選擇JPG圖片進行上傳", type="jpg")
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption='Uploaded image.', use_column_width=True)
#         st.write("")
#         st.write("分類中...")
#         label = classification(image)
            
#         st.write("此圖片預測類別為 : {}".format(label))
        
# elif st.button("ocr"):
    
st.title('圖片OCR轉文字')
st.header("OCR: Optical Character Recognition")
st.text('請上傳圖片進行OCR')
    
    
uploaded_file = st.file_uploader("選擇圖片進行上傳", type=["png", "jpg"], key = "ocr_image_uploader")
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded image.', use_column_width=True)
        st.write("")
        st.write("檢測中...")
        text, time_cost, draw_image = get_text(image)
            
        st.write("總共花費時間: {:.3f}s".format(time_cost))
        st.image(draw_image, caption = "偵測結果")
        st.write("偵測到的文字 : ")
        st.write(text)

            
            