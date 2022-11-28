FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
COPY /main.py .
EXPOSE 5000
CMD python main.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]