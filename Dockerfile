FROM python:3.7

RUN adduser --disabled-password --gecos "" dockeruser
USER dockeruser

WORKDIR /home/dockeruser/app
ENV PATH="/home/dockeruser/.local/bin:${PATH}"

COPY requirements.dev.txt requirements.dev.txt 
RUN pip install --user -r requirements.dev.txt

# As per https://github.com/squidfunk/mkdocs-material/blob/6d678a4a66a6d4d4a45a62331767a5c7beaa507f/Dockerfile
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
