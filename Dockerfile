FROM python
WORKDIR /app
COPY pipeline.py pipeline_new.py
COPY data.csv source.csv
RUN pip install pandas
ENTRYPOINT ["python","pipeline_new.py", "source.csv", "out.csv"]
#VOLUME ["/Bunker"]
