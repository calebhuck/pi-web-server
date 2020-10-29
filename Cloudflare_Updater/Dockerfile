FROM python:3

ADD UpdateCloudflareDNS.py /
ADD key.key /
ADD email.key /

RUN pip install cloudflare

CMD ["python3", "./UpdateCloudflareDNS.py"]