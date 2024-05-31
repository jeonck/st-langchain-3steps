# https://python.langchain.com/v0.1/docs/expression_language/get_started/
# https://python.langchain.com/v0.1/docs/get_started/quickstart/
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 애플리케이션 제목 설정
st.title("영어 회화 생성기")

# 사이드바에 OpenAI API 키 입력 필드 추가
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요:", type="password")

# 주제 입력 필드 추가
agenda = st.text_input("주제를 입력하세요:", "저는 식당에 가서 음식을 주문하고 싶어요")

# 프롬프트 템플릿 정의
template = """
당신은 영어를 가르치는 10년차 영어 선생님입니다. 주제에 대해 [FORMAT]으로 영어 회화를 작성해 주세요.
주제: {agenda}
FORMAT:
- 영어 회화:
- 한글 해석:
"""
prompt = PromptTemplate.from_template(template)

# OpenAI 채팅 모델 초기화
if api_key:
    model = ChatOpenAI(
        model="gpt-4o",
        max_tokens=2048,
        temperature=0.1,
        api_key=api_key  # API 키 설정
    )

    # 문자열 출력 파서 초기화
    output_parser = StrOutputParser()

    # 프롬프트, 모델, 출력 파서를 연결하여 처리 체인 구성
    chain = prompt | model | output_parser

    # 버튼 클릭 시 체인 실행
    if st.button("생성하기"):
        result = chain.invoke({"agenda": agenda})
        st.write("### 결과:")
        st.write(result)
else:
    st.warning("사이드바에서 API 키를 입력하세요.")
