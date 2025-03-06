from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage

messages = [AIMessage(content="hi how can i help you?", name="Model")]
messages.append(HumanMessage(content="add 2 and 5 and then mulitply by 10 and divivde by 7", name="Lance"))

#for m in messages:
 #   m.pretty_print()
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3.1:latest")
max_iterations =1
iteration = 0
result = llm.invoke(messages)
messages.append(AIMessage(content=result, name="Model"))
iteration += 1
print(result)
print(".......................")
ans=llm.invoke(result)
print(ans)
