FROM python:latest

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN chmod +x gitleaks
RUN chmod +x gh

EXPOSE 5000

CMD ["python", "app.py"]