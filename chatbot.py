from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage
from langchain_ollama import OllamaLLM

# Initialize messages with a greeting from the model
messages = [AIMessage(content="hi how can i help you?", name="Model")]

# Initialize the language model
llm = OllamaLLM(model="llama3.1:latest")

# Main loop to handle user input
while True:
    # Get user input
    question = input("ques: ")
    if question.lower() == "bye":
        for m in messages:
            pprint(m)
        break
    else:
        messages.append(HumanMessage(content=question, name="sravan"))
        
        # Invoke the language model with the current messages
        result = llm.invoke(messages)
        
        # Append the model's response to the messages
        messages.append(AIMessage(content=result, name="Model"))
        
        # Print the result
        print(result)
