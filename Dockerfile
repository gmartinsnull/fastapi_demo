FROM python:3.12-slim

WORKDIR .

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

CMD ["fastapi", "run", "api/main.py", "--host", "0.0.0.0", "--port", "80"]