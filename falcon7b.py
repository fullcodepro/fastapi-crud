

from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import os
# huggingfacehub_api_token = os.environ['HUGGINGFACEHUB_API_TOKEN']
huggingfacehub_api_token = "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"


repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                     repo_id=repo_id,
                     model_kwargs={"temperature": 0.6, "max_new_tokens": 2000})

template = """
You are an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

{question}

"""


async def factory(question):
    print({question})
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=False)
    respuesta = llm_chain.run(question=question)
    print(respuesta)
    return respuesta

# result = factory("What is the meaning of life?")
# print(result)