FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /tutor
WORKDIR /tutor
ADD requirements.txt /tutor/
RUN pip install -r requirements.txt
ADD . /tutor/
