# Automated Ingestion Script
## General Info
This script can ingest .csv data into postgresql databases .
The aim of the project however, is to ingest data of any 
**_format_** into any **_database_**. At present, working on 
the plugins for different formats (i.e. inputs) and 
databases (i.e. outputs).

## Technologies
The script is developed in Python.

## Setup
1. Modify **_src/database.ini_** with your own database credentials. 
2. Drop the data into _**data/to_ingest**_ folder.
3. Run **_ingest.sh_**

and DONE!! The data is ingested.

## Status
1. Working to create plugins that allow ingesting data
of any type (such as .parquet, .xml, .xlsx, .tsv).
2. Also working to create plugins that allow ingesting
into any type of database (such as PostgreSQL, mySQL, MariaSQL, 
MSSQL)