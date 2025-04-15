import gradio as gr
from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage
from langchain_ollama import OllamaLLM

# Initialize messages with a greeting from the model
messages = [AIMessage(content="hi how can i help you?", name="Model")]

# Initialize the language model
llm = OllamaLLM(model="llama3.1:latest")

def chat_with_model(question):
    if question.lower() == "bye":
        return "\n".join([f"{m.name}: {m.content}" for m in messages])
    else:
        messages.append(HumanMessage(content=question, name="sravan"))
        result = llm.invoke(messages)
        messages.append(AIMessage(content=result, name="Model"))
        return result

# Create Gradio interface
iface = gr.Interface(
    fn=chat_with_model,
    inputs="text",
    outputs="text",
    title="Chat with Model",
    description="Ask anything and get responses from the model."
)

# Launch the interface
iface.launch(share=True)
