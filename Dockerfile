FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0", "-w", "1", "src.predict_app:app"]
EXPOSE 8000