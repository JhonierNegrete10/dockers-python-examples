FROM python:3.10.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install fastapi uvicorn 

COPY tmp.py .

CMD ["/opt/venv/bin/uvicorn", "tmp:app", "--reload", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000