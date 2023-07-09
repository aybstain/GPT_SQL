# Audio-to-SQL Conversion Project

This project utilizes speech recognition, natural language processing, and database interaction to convert spoken queries into SQL queries and retrieve data from a SQLite database.

## Prerequisites

Before running the code, ensure that you have the following dependencies installed:

- Python (version 3.6 or above)
- Other required libraries (specified in the `requirements.txt` file)

To install the required libraries, you can use the following command:

```bash
pip install -r requirements.txt
```


## Project Structure

The project consists of four key functions:

1. **Speech-to-Text Conversion**: `speech_to_text()` captures speech input from the microphone and converts it into text using the Google Speech Recognition API.

2. **Query-to-SQLite**: `query_to_sqlite(database_path, csv_file_path, table_name, sql_query)` sets up a SQLite database, imports data from a CSV file, and executes a provided SQL query on the database.

3. **Text-to-SQL Conversion**: `text_to_sql(table_name, text, column_names)` generates an SQL query using the OpenAI GPT API based on the provided text, table name, and column names.

4. **Audio-to-SQL Conversion**: `audio_to_sql(database_path, csv_file_path, table_name)` combines speech recognition, text-to-SQL conversion, and query execution to convert spoken queries into SQL queries, execute them on the SQLite database, and retrieve the results.

## Usage

To utilize this project, follow these steps:

1. Create a virtual environment for the project (optional but recommended).

2. Install the required libraries by running the previous command

3. Prepare your CSV file containing the data to be imported into the SQLite database.

4. Set the appropriate paths and table name in the `audio_to_sql` function call.

5. Execute the `audio_to_sql` function to start the audio-to-SQL conversion process.

## demo
1. Specify the paths :

   <img width="274" alt="Capture" src="https://github.com/aybstain/GPT_SQL/assets/103702856/aed20408-d872-4418-8918-7d8aa07f05eb">
   
3. Run the function :

   <img width="293" alt="Capture1" src="https://github.com/aybstain/GPT_SQL/assets/103702856/9fe54447-3e62-4273-ae4a-57a493e6c4b2">

   Check the speech and the sql_query :

   <img width="536" alt="Capture2" src="https://github.com/aybstain/GPT_SQL/assets/103702856/9daee2d3-fe39-4fc1-97d9-a2695e3e27af">
   
5. View the result :

   <img width="345" alt="capture3" src="https://github.com/aybstain/GPT_SQL/assets/103702856/baf25ea8-ad7e-4034-af1d-880263f990cb">



## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests to enhance the functionality, improve documentation, or suggest new features.

## License

This project is licensed under the [MIT License](LICENSE).







