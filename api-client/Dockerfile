FROM python:3.10-slim-buster

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY change_client.py ./

CMD ["python", "change_client.py"]