FROM fuzzers/atheris:2.0.7-python3.9

# Install dependencies.
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y git
ADD . /src
WORKDIR /src
RUN pip3 install .

CMD ["/src/mayhem/fuzz_human.py"]
