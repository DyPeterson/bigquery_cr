## Cloud Database Cleaning & Queries

### Contributors:

- [Dylan Peterson](https://github.com/DyPeterson)

### Description

A [Data Stack Academy](https://www.datastack.academy/) code review project to load a CSV into a pandas dataframe and upload to the cloud (Google BigQuery & Google Cloud Storage) and queries that data with SQL.

### Technologies Used:

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Google BigQuery](https://console.cloud.google.com/bigquery)
- [Google Cloud Storage](https://console.cloud.google.com/)

#### Programs used:

- [Visual Code Studio](https://code.visualstudio.com/)

- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US) ( Running: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) ([ubuntu 20.04](https://releases.ubuntu.com/20.04/)))


### Setup & Installation:


1. Through the terminal like [GitBash](https://git-scm.com/downloads)

  
	1. Open the terminal and navigate to where you would like the new project to be using `cd` commands. Its also recommended that you make a new directory using `mkdir *directory-name*`.


	1. Clone the repository using the command `git clone https://github.com/DyPeterson/bigquery_cr.git`


	1. After cloning the directory it will appear in the directory that your terminal is set to. So make sure you are in the directory that you want this project copied to.


	1. Once this project is cloned you can navigate to that folder within your terminal and create a virtual environment `python3.7 -m venv *any-name*`. Now activate the venv with `source *any-name*/bin/activate`


	1. Install requirements in venv `pip install -r requirements.txt`


	1. Download the data by running the `get_data.sh` either by clicking it or running in the terminal.


	1.  `code .` to open in default coding software.

  

2. Through GitHub.com

	
	1. Go to the project's directory page **[HERE](https://github.com/DyPeterson/bigquery_cr.git)**


	2. Click the green `code` button to open the drop-down menu.


	3. At the bottom of the menu will have *Download Zip*. Go ahead and click it to download the project.


	4. Once downloaded find the `.zip` file and right-click it to bring up the menu. Within that menu click `Extract Here` to extract it in the current folder or click `Extract Files...`to select which folder you would like the project in.


	5. Once the project has been extracted, locate the folder in a terminal and open it with `code .` .
	6.  Download CSVs with either: 
		1. Following terminal commands:
		-  ` mkdir ./data`
		 - `gsutil -m cp gs://netflix_titles_dpeterson/netflix_titles.csv ./data`

		 2. Following one of the links listed below:
		 - [Google Cloud Storage](https://storage.googleapis.com/netflix_titles_dpeterson/netflix_titles.csv)
		- [kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
	7. Run the `main.py`  with the command `python main.py`to transform the database and upload to a new CSV `clean_netflix.csv`

### Useful Links

#### Link to project on GitHub:
[GitHub Repository](https://github.com/DyPeterson/bigquery_cr)
#### Links to Dataset:
[Google Cloud Storage](https://storage.googleapis.com/netflix_titles_dpeterson/netflix_titles.csv)
[Google Cloud Storage gsutil](gs://netflix_titles_dpeterson/netflix_titles.csv)
[kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

### Details

Takes a CSV file from the internet and loads it into a pandas dataframe. From there the program runs cleaning operations on the dataframe. With the cleaned dataframe it then creates a new CSV file with all the cleaning operations ran onto it. I then took the new CSV and uploaded it to the cloud, both Google Cloud Storage and Google BigQuery. With it uploaded to BigQuery I ran the queries listed in the `queries.sql` to gather different types of information based on the data.

Contact me with any questions or suggestions [Here](dylan.peterson17@gmail.com)

### Known Bugs

 No known bugs at this time.

### Copyright 2022


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.