import configparser
import os
import logging
import gradio as gr
from modules.agent_creation import create_agent
from modules.query_execution import execute_query, save_response_to_excel
from io import StringIO
import re
from contextlib import redirect_stdout

class StringIOHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_capture_string = StringIO()

    def emit(self, record):
        self.log_capture_string.write(self.format(record) + '\n')

    def get_log_contents(self):
        return self.log_capture_string.getvalue()

log_capture_handler = StringIOHandler()
logging.basicConfig(handlers=[log_capture_handler], level=logging.INFO)

def strip_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def main(query):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    input_file = config['PATH']['INPUT_FILE']
    output_file = config['PATH']['OUTPUT_FILE']
    
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found.")
        return
    
    csv_path = "data/credit_data.csv"
    log_capture_handler.log_capture_string.truncate(0)
    log_capture_handler.log_capture_string.seek(0)
    stdout_capture_string = StringIO()
    
    with redirect_stdout(stdout_capture_string):

        agent = create_agent(csv_path)
        try:
            response = agent(query)
            logs = log_capture_handler.get_log_contents()
            stdout = stdout_capture_string.getvalue()
        except Exception as e:
            print(f"Error during query execution: {e}")
        
    save_response_to_excel(response, output_file)
    print(f"Response saved to {output_file}")

    cleaned_logs = strip_ansi_escape_sequences(logs + stdout)

    return response["output"], cleaned_logs, csv_path

if __name__ == "__main__":
    
    iface = gr.Interface(
        fn=main,
        inputs=gr.Textbox(lines=2, placeholder="🔍 Enter your query here...", label="Query Input 📥"),
         outputs=[
        gr.Textbox(label="Query Response 📊"),
        gr.Textbox(label="Verbose Logs 📝"),
        gr.File(label="Download Processed CSV 📂")
        ],
        title="💡 Data Extractor",
        description="🔧 This tool extracts and processes data based on your query. Enter your query in the input box below and click submit. ⏩",
        examples=[
            ["💰 What is the total credit balance?"],
            ["📅 Show me the sum of credit amount for 2024 May."],
            ["👥 How many unique customers are there?"],
            ["📈 What is the average credit balance?"],
        ]
    )
    
    iface.launch(share=True)
