FROM python:3.14.8

# アプリケーションディレクトリを作成する
WORKDIR /usr/src/python_django
# アプリケーションコードをコンテナにコピー
COPY . /usr/src/python_django

RUN apt-get update && \ 
    apt-get install -y libgl1-mesa-dev && \
     pip install --upgrade pip && \ 
     pip install pipenv && \
     pipenv install --system

# コンテナのポート5000を公開
EXPOSE 8000

# 開発用サーバーの起動
CMD ["python", "./django_sample/manage.py", "runserver", "0.0.0.0:8000"]
