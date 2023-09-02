# SQL Chinook Database Explorer
The purpose of this project is to explore the Chinook database using SQL queries. The Chinook database is a sample SQLite database that contains information about a fictional music store, including data on customers, tracks, albums, and more.

In order to set up and run this project, please complete the following steps:

1) Clone the Repository

`git clone git@github.com:bloominstituteoftechnology/basic_sql_queries.git`

2) Activate the Virtual environment

`pipenv shell`

3) Execute the queries in `queries.py` against the `chinook.db` SQLite database by running `connect.py` from the command line

`python connect.py`

You should see the questions and their corresponding answers printed out to the command line.

Below is a Schema Diagram that will aid you in understanding the structure of the database.

![Schema Diagram](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)

## Optional

You may also download the desktop software DB Browser to assist you in drafting successful queries. DB Browser provides better insight into table schemas and gives better syntax highlighting for queries than `.py` files.

[DB Browser for SQLite](https://sqlitebrowser.org/dl/)
