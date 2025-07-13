from redhat/ubi8
run yum install python3 -y
workdir /root/
copy app.py app.py
run pip install flask
entrypoint ["python3","app.py"] 