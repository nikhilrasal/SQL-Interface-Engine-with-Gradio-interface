# SQL-Interface-Engine-with-Gradio-interface

1. Developed a system using the OpenAI API to translate natural language queries into optimized SQL queries, enhancing user in- teraction with databases through natural language inputs.

2. Implemented a robust function to generate SQL queries with error handling and retry mechanisms, ensuring high accuracy and reliability in the generated queries.
   
3. This project democratizes data access by enabling users to interact with databases using natural language queries through a user-friendly Gradio interface. This eliminates the need for SQL expertise, empowering users to easily explore and analyze their data, gaining valuable insights with greater efficiency.

"""
# SQL Assistant with Gradio Interface

This script allows you to interact with a MySQL database using natural language queries. 
It uses OpenAI's GPT model to generate SQL queries based on user input and displays the results through a Gradio web interface.

## Steps to Use

1. **Setup Requirements**:
   - Install required Python libraries:
     ```
     pip install pymysql openai gradio
     ```
   - Add your database credentials (`host`, `user`, `password`, `database`) and OpenAI API key in the script.

2. **Configuration**:
   - Update the following variables in this script:
     ```python
     host = "your_database_host"
     user = "your_database_user"
     password = "your_database_password"
     database = "your_database_name"
     openai.api_key = "your_openai_api_key"
     ```

3. **Run the Script**:
   - Save this file as `run_sql.py`.
   - Execute the script:
     ```
     python run_sql.py
     ```

4. **Access the Gradio Application**:
   - Open your browser and go to: [http://127.0.0.1:8000/gradio/](http://127.0.0.1:8000/gradio/).

5. **How to Use**:
   - Enter your natural language query in the Gradio interface.
   - The application will:
     - Generate an SQL query.
     - Execute it on the database.
     - Display the results or errors in the output box.

## Example Query
- Input: "Show all records from the employees table."
- Output: The SQL query and the results from the database.
"""
