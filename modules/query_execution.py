import pandas as pd

def execute_query(agent, query):

    try:
        response = agent.invoke(query)
        output = response["output"]
        return output
    except Exception as e:
        print(f"Error executing query: {e}")
        raise
    
def save_response_to_excel(response, output_file):
    try:
        df = pd.DataFrame([response], columns=["Response"])
        df.to_excel(output_file, index=False, engine='openpyxl')
    except Exception as e:
        print(f"Error saving Excel: {e}")
        raise
