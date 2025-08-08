import gradio as gr
import os
import datetime

def greet(name):
    return f"Hello {name}! 👋"

def current_time():
    return f"🕒 Current time is: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def list_files():
    return "\n".join(os.listdir("."))

def run_linux_command(command):
    try:
        output = os.popen(command).read()
        return output
    except Exception as e:
        return str(e)

with gr.Blocks(title="Automation Panel") as demo:
    gr.Markdown("# ⚙️ Automation Panel with Gradio")

    with gr.Tab("Greet"):
        name_input = gr.Textbox(label="Enter your name")
        greet_btn = gr.Button("Say Hello")
        greet_output = gr.Textbox(label="Greeting")
        greet_btn.click(fn=greet, inputs=name_input, outputs=greet_output)

    with gr.Tab("System Time"):
        time_btn = gr.Button("Show Current Time")
        time_output = gr.Textbox(label="Current Time")
        time_btn.click(fn=current_time, inputs=[], outputs=time_output)

    with gr.Tab("File Browser"):
        file_btn = gr.Button("List Files in Current Dir")
        file_output = gr.Textbox(label="Files", lines=10)
        file_btn.click(fn=list_files, inputs=[], outputs=file_output)

    with gr.Tab("Run Linux Command"):
        cmd_input = gr.Textbox(label="Enter Linux Command")
        cmd_btn = gr.Button("Run Command")
        cmd_output = gr.Textbox(label="Command Output", lines=10)
        cmd_btn.click(fn=run_linux_command, inputs=cmd_input, outputs=cmd_output)

demo.launch()
