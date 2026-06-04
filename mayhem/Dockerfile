FROM python:3.11-slim

# Install dependencies.
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y git && \
        pip3 install atheris
ADD . /src
WORKDIR /src
RUN pip3 install .

CMD ["/src/mayhem/fuzz_human.py"]
