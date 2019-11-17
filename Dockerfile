FROM centos:7
LABEL author="Truong Bui Van"

WORKDIR /root
COPY app.py .
COPY requirements.txt .

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y python-pip
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]


