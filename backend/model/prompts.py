generation_question_prompt = """다음 글의 주요 내용을 간결하게 요약하여 구글에서 검색할 것 같은 핵심 키워드 단어 5개로 추출하세요. 
각 키워드는 원문의 내용을 뉴스로 찾기 쉽도록 가장 중요한 정보를 담아야 합니다. 
결과는 리스트 형태로 작성해주세요.
반드시 한국어로 답합니다.

글:
{content}"""

fake_news_detection_prompt = """당신은 AI 분석가입니다. 주어진 글과 검색된 영어 뉴스 내용을 비교하여, 두 텍스트 사이의 차이점을 찾고 한글로 답변해주세요.
다음 지침에 따라 작업을 수행하세요:

주제의 차이점: 두 텍스트가 다루는 주제에서 차이가 있는지 확인하세요.
주장 및 관점: 주요 주장이나 관점이 서로 다른지 분석하세요.
답변 언어: 텍스트의 차이점을 찾고 반드시 한국어로 답변해주세요.
글:
{content}

뉴스 내용:
{news}"""