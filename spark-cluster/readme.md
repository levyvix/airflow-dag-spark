cd spark-cluster

docker build -t owshq-spark:3.5 -f Dockerfile.spark . 

docker-compose up -d