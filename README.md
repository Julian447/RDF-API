# RDF-API-Tool
An self hosted API toolfor using RDF as database

## Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```
uvicorn main:app --reload --host "INSERT HOST" --port INSERT PORT
```
If running on linux, use this to run as background process
```
uvicorn main:app --reload --host "INSERT HOST" --port INSERT PORT &
```

## Usage
Any project which interacts with the api needs to do one of:
- Set up pydantic models like in './rdf_api/datastructure/', or
- Set up an equivelant json







