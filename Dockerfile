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

RUN python ./django_sample/manage.py collectstatic --noinput

# コンテナのポート5000を公開
EXPOSE 8000

# 開発用サーバーの起動
# CMD ["python", "./django_sample/manage.py", "runserver", "0.0.0.0:8000", "--insecure"]
# CMD ["gunicorn", "django_sample.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
CMD ["gunicorn", "--chdir", "django_sample", "django_sample.wsgi:application", "--bind", "0.0.0.0:8000", "--reload", "--workers", "3", "--access-logfile", "-", "--error-logfile", "-"]