import streamlit as st
import pandas as pd
import os

# 1. 화면 설정
st.set_page_config(layout="wide", page_title="나만의 포트폴리오")

# 2. 엑셀 파일 읽기
try:
    df = pd.read_excel("data.xlsx", header=0)
except FileNotFoundError:
    st.error("엑셀 파일이 없습니다.")
    st.stop()

# ==========================================
# [기능 1] 페이지 상태 관리
# ==========================================
if 'view_mode' not in st.session_state:
    st.session_state['view_mode'] = 'list'
    st.session_state['selected_index'] = None

def go_home():
    st.session_state['view_mode'] = 'list'

# ==========================================
# [화면 1] 작품 목록 (갤러리 뷰)
# ==========================================
if st.session_state['view_mode'] == 'list':
    st.title("🎨 My Design Portfolio")
    st.write("감상하고 싶은 작품을 선택해주세요.")
    st.divider()

    # 3단 배열
    cols = st.columns(3) 

    for i in range(len(df)):
        with cols[i % 3]: 
            title = df.iloc[i]['주제']
            img_file = df.iloc[i]['파일명']
            img_path = f"images/{img_file}"
            
            # (1) 이미지 보여주기
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.write("이미지 없음")

            # (2) [핵심 수정] 꽉 차는 버튼 만들기
            # 버튼이 이미지 바로 밑에 붙어서, 마치 카드를 누르는 느낌을 줍니다.
            if st.button(f"🔍 {title} (클릭)", key=f"btn_{i}", use_container_width=True):
                st.session_state['view_mode'] = 'detail'
                st.session_state['selected_index'] = i
                st.rerun()

# ==========================================
# [화면 2] 상세 화면
# ==========================================
elif st.session_state['view_mode'] == 'detail':
    idx = st.session_state['selected_index']
    row = df.iloc[idx]
    
    img_path = f"images/{row['파일명']}"
    
    # 상단 메뉴
    col_back, col_empty = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ 목록으로 (Back)", use_container_width=True):
            go_home()
            st.rerun()

    st.divider()
    
    # 상세 내용 (왼쪽:그림 / 오른쪽:설명)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_path):
            st.image(img_path, caption=row['주제'], use_container_width=True)
            
            # 팝업 확대 기능
            @st.dialog("작품 원본 보기")
            def popup_img():
                st.image(img_path)
            
            if st.button("🔍 더 크게 보기 (Popup)", use_container_width=True):
                popup_img()

    with col2:
        st.header(row['주제'])
        st.info("작품 설명")
        st.write(row['설명'])