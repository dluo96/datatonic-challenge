# An analysis of the TMDB movies

Analysis and model prediction of movie revenue using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata/data).

## Setup

- install pipenv if not installed yet: `pip install pipenv`
- navigate to repo and run command:
```
pipenv install
pipenv shell
```

## Usage

### Executing all notebooks at once
```
python run.py
```
### Executing notebooks in a certain folder
```
python run.py (folder_name)
```
## Development

Run jupyter from local host using:
```
jupyter notebook \ --NotebookApp.allow_origin='https://colab.research.google.com' \ --port=8888 \ --NotebookApp.port_retries=0
```