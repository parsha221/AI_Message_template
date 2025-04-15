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

def display_history():
    return "\n".join([f"{m.name}: {m.content}" for m in messages])

# Create Gradio interface using Blocks
with gr.Blocks() as demo:
    chat_input = gr.Textbox(label="Ask anything")
    chat_output = gr.Textbox(label="Response")
    history_button = gr.Button("Show History")
    history_output = gr.Textbox(label="Conversation History")

    def update_chat(question):
        response = chat_with_model(question)
        return response

    def show_history():
        history = display_history()
        return history

    chat_input.submit(update_chat, inputs=chat_input, outputs=chat_output)
    history_button.click(show_history, outputs=history_output)

demo.launch(share=True)
