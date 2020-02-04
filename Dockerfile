FROM python:3.8.1-buster
COPY requirements.txt .
run pip3 install -r requirements.txt
COPY . /vibecheck
WORKDIR /vibecheck
EXPOSE 5000
CMD python ./vibecheck.py
