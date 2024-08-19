
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api.py /code/api.py

CMD ["fastapi", "run", "api.py", "--port", "80"]
