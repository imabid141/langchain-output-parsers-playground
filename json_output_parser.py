from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",   # "Qwen/Qwen3-Coder-Next"
    task="text-generation",
    temperature=0.2,   
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Without chain
# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result['name'])
# print(type(final_result))

# With chain
chain = template | model | parser

result = chain.invoke({'topic':'cyber security'})

print(result)