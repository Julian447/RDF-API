# RDF-API
A self hosted API tool for using RDF as a remote database
This is a project meant to experiment with handling the transmitting RDF through HTTP  

## Setup
Run the "setup.sh" script or use the following commands:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
Either run the "start_api.sh" script or directly from "main.py"
**remember to replace host and port with your preferred ones**

This can also be directly run from uvicorn:
```
uvicorn main:app --reload --host "INSERT HOST" --port INSERT PORT
```


## Usage
Any project which interacts with the api needs to do one of:
- Set up pydantic models like in './rdf_api/datastructure/', or
- Set up an equivelant json







