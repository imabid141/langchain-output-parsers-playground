from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# LLM 1: Report generation (slightly creative)
llm_report = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation",
    temperature=0.3,
    max_new_tokens=700
)

# LLM 2: Summary generation (more deterministic)
llm_summary = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation",
    temperature=0.1,
    max_new_tokens=300
)

model_report = ChatHuggingFace(llm=llm_report)
model_summary = ChatHuggingFace(llm=llm_summary)

# Prompt 1: Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on the {topic}.",
    input_variables=["topic"]
)

# Prompt 2: Summary
template2 = PromptTemplate(
    template="Write a concise 10-line summary of the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Chain
chain = (
    template1
    | model_report
    | parser
    | {"text": RunnablePassthrough()}
    | template2
    | model_summary
    | parser
)

# Invoke
result = chain.invoke({"topic": "black hole"})
print(result)
