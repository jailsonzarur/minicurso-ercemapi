from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='Qwen/Qwen3-30B-A3B',
    base_url='https://api.sobdemanda.mandu.piaui.pro/',
    api_key='sk-BjoLcsMsPQMQ0vGvvy5AAQ',
    temperature=0.1
)