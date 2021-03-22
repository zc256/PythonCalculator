FROM python:3

ADD . .

CMD ["python", "./testCalculator.py"]