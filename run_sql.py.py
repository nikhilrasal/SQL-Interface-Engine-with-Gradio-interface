import pymysql
import openai
import gradio as gr

# Database and OpenAI configuration
host = "localhost"
user = "root"
password = "norahealthai"
database = "nora"

openai.api_key = "Add your openai key"

# Define the function signature for OpenAI's function calling
functions = [
    {
        "name": "generate_sql_and_rephrase",
        "description": "Generates an SQL query based on a natural language query.",
        "parameters": {
            "type": "object",
            "properties": {
                "sql_query": {
                    "type": "string",
                    "description": "The SQL query generated from the natural language input."
                },
            },
            "required": ["sql_query"]
        }
    }
]

def generate_sql_and_rephrase(natural_language_query, sql_result=None):
    """
    Generate SQL and rephrase the result using a single OpenAI API call with function calling.
    """
    messages = [
        {
            "role": "system",
            "content": "You are a data analyst assistant that generates SQL queries."
        },
        {
            "role": "user",
            "content": natural_language_query
        }
    ]

    if sql_result:
        messages.append({
            "role": "assistant",
            "content": f"SQL Result: {sql_result}"
        })

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions=functions,
        function_call={"name": "generate_sql_and_rephrase"},
        temperature=0.5
    )

    return response["choices"][0]["message"]["function_call"]["arguments"]

def execute_sql_query(query):
    """
    Execute the SQL query on the database and return results.
    """
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Exception as e:
        return f"Error executing SQL query: {str(e)}"
    finally:
        connection.close()

def chat_with_sql_gradio(user_query):
    """
    Handle a single user query using Gradio.
    """
    try:
        # Generate SQL and optionally rephrase
        response = generate_sql_and_rephrase(user_query)

        # Parse the SQL query from the response
        sql_query = eval(response).get("sql_query", "").strip()
        if sql_query and not sql_query.endswith(";"):
            sql_query += ";"

        # Execute the SQL query
        results = execute_sql_query(sql_query)
        if results and not isinstance(results, str):
            return f"SQL Query: {sql_query}\nResults: {results}"
        else:
            return f"SQL Query: {sql_query}\nError executing SQL query or no results found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
interface = gr.Interface(
    fn=chat_with_sql_gradio,
    inputs=gr.Textbox(lines=3, label="Enter your question:"),
    outputs=gr.Textbox(label="Response"),
    title="SQL Assistant",
    description="Ask questions in natural language, and the assistant will generate SQL queries and execute them on the database."
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()
