from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation",
    temperature=0.2,   
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)

# 1st Prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed repot on the {topic}",
    input_variables=['topic']
)

# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template="write a 5 lines summary on the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
