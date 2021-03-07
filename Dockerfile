FROM ersiliaos/ersilia-service:0.1.0
MAINTAINER ersilia

RUN pip install git+https://github.com/bp-kelley/descriptastorus
RUN pip install chemprop==1.1.0
WORKDIR /repo
COPY . /repo