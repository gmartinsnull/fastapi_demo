FROM python:3.12

WORKDIR .

COPY ./requirements.txt ./app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

COPY . ./app

CMD ["fastapi", "run", "app/api/main.py", "--port", "80"]