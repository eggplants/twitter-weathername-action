FROM python:latest

ADD src /src
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN chmod +x src/main.py

ENTRYPOINT ["/src/main.py"]