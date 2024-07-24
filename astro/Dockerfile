FROM quay.io/astronomer/astro-runtime:11.7.0

USER root

RUN apt update && \
	apt-get install -y openjdk-11-jdk && \
	apt-get install -y ant && \
	apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

