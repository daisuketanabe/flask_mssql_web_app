# SAMPLE FLASK MSSQL WEB APP #
This is a sample Python project that uses Flask and MSSQL to build a web application.
## Prerequisite ##
- Python 3.x: 
  * https://www.python.org/downloads/
- Microsoft SQL Server 2022
  * Windows:
    1. https://www.microsoft.com/en-gb/sql-server/sql-server-downloads
  * Mac: 
    1. https://www.docker.com/products/docker-desktop/
    2. https://hub.docker.com/_/microsoft-azure-sql-edge
- ODBC Driver 17 for SQL SERVER
  * https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
- Azure Data Studio or any DBMS:
  * https://learn.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio
## Installation ##
1. Clone the repository: 
git clone https://github.com/daisuketanabe/flask_mssql_web_app.git
2. Navigate to the project directory:
```{python} 
cd flask_mssql_web_app
```
3. Create a virtual environment: 
```{python}
python -m venv env
```
4. Activate the virtual environment:
 * Windows: 
 ```{python}
 env\Scripts\activate.bat
 ```
 * Unix/Mac: 
 ```{python} 
 source env/bin/activate
 ```
5. Install dependencies: 
```{python}
 pip install -r requirements.txt
 ```
6. Create a database in MSSQL using __DemoDB.sql file__
7. Update the database configuration in config.py with your MSSQL database details.
## Usage ##
1. Activate the virtual environment:
- Windows: env\Scripts\activate.bat
- Unix/Mac: source env/bin/activate
2. Run the Flask app: 
```{python}
python app.py
```
3. Open your web browser and go to http://localhost:5000 to view the app.
## Project Structure ##
* app.py: Main Flask application file.
* config.py: Configuration file for the app, including database details
* sample_config.py: Sample config.py file
* DemoDB.sql: Sample MSSQL Dump file.
* requirements.txt: List of Python dependencies.
* templates/: Directory containing HTML templates for the app.
* README.md: This file.
## Contribution ##
If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch: git checkout -b my-new-feature
3. Make your changes and commit them: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request.
## License ##
This project is licensed under the MIT License. 
