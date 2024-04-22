FROM centos

COPY . /home/myblog/

WORKDIR /home/myblog/

RUN sudo yum update

RUN sudo yum install python3.8

RUN pip install -r requirements.txt

ENV PYTHONPATH=/home/myblog/

ENTRYPOINT ["python","main.py"]
