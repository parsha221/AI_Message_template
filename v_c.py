import gradio as gr

def print_abc(abc):
    # Print abc in the terminal
    print(abc)
    # Return abc to be displayed in Gradio
    return abc

# Create Gradio interface
iface = gr.Interface(
    fn=print_abc,
    inputs="text",
    outputs="text",
    title="Print ABC",
    description="Enter a string and click submit to print it.",
    live=False
)

# Launch the interface with share=True
iface.launch(share=True)
