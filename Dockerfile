FROM python:3.7
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

#RUN apt-get update
#RUN apt-get install vim

COPY src /app/src
ENV PYTHONPATH=/app
WORKDIR /app/

EXPOSE 8000
CMD ["apt-get update","apt-get install vim"]
#ENTRYPOINT ["uvicorn"]
#CMD ["src.main:app", "--host", "0.0.0.0"]