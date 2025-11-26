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
# [기능 1] 페이지 상태 관리 (목록 vs 상세)
# ==========================================
# 'view_mode'가 'list'면 목록을, 'detail'이면 상세화면을 보여줍니다.
if 'view_mode' not in st.session_state:
    st.session_state['view_mode'] = 'list'
    st.session_state['selected_index'] = None

# 홈 버튼(로고) 누르면 목록으로 돌아가는 함수
def go_home():
    st.session_state['view_mode'] = 'list'

# ==========================================
# [화면 1] 작품 목록 (갤러리 뷰)
# ==========================================
if st.session_state['view_mode'] == 'list':
    st.title("🎨 My Design Portfolio")
    st.write("작품을 클릭하면 상세 내용을 볼 수 있습니다.")
    st.divider()

    # ★ 핵심: 3개의 기둥(Column)을 만듭니다.
    cols = st.columns(3) 

    # 엑셀 데이터만큼 반복
    for i in range(len(df)):
        # 3개의 기둥에 순서대로 배분 (0, 1, 2, 0, 1, 2...)
        with cols[i % 3]: 
            # 데이터 가져오기
            title = df.iloc[i]['주제']
            img_file = df.iloc[i]['파일명']
            img_path = f"images/{img_file}"
            
            # (1) 이미지 보여주기
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.error("이미지 없음")

            # (2) 주제(제목) 표시
            st.subheader(title)

            # (3) '상세보기' 버튼
            # 버튼을 누르면 view_mode를 'detail'로 바꾸고, 몇 번째인지 기억함
            if st.button(f"🔍 {title} 자세히 보기", key=f"btn_{i}"):
                st.session_state['view_mode'] = 'detail'
                st.session_state['selected_index'] = i
                st.rerun() # 화면 즉시 새로고침

# ==========================================
# [화면 2] 상세 화면 (크게 보기)
# ==========================================
elif st.session_state['view_mode'] == 'detail':
    # 선택된 번호(index)의 데이터 가져오기
    idx = st.session_state['selected_index']
    row = df.iloc[idx]
    
    img_path = f"images/{row['파일명']}"
    
    # [상단] 뒤로가기 버튼
    if st.button("⬅️ 목록으로 돌아가기"):
        go_home()
        st.rerun()

    st.divider()
    
    # 화면을 1:1로 나눠서 왼쪽엔 그림, 오른쪽엔 설명 배치
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_path):
            st.image(img_path, caption=row['주제'], use_container_width=True)
            
            # (추가) 여기서도 팝업으로 더 크게 보고 싶다면
            @st.dialog("이미지 원본")
            def popup_img():
                st.image(img_path)
            
            if st.button("크게 보기 (팝업)"):
                popup_img()

    with col2:
        st.title(row['주제'])
        st.info("작품 설명")
        st.write(row['설명'])