FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r  /app/requirements.txt
EXPOSE 5000
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]