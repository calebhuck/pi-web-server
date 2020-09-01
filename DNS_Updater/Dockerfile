FROM python:3

ADD GoDaddyUpdateDNS.py /
ADD key.key /
ADD secret.key /

RUN pip install godaddypy

CMD ["python3", "./GoDaddyUpdateDNS.py"]