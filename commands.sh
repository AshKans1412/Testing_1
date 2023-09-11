docker build -t python-pandas-test-1 .

docker volume create Bunker

docker run -it --mount source=Bunker,target=/app python-pandas-test-1

#python pipeline_new.py source.csv out.csv
