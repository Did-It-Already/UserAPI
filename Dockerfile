FROM python:3

ENV CLOUDINARY_API_KEY=171759724969595
ENV CLOUDINARY_API_SECRET=12LboDYtu51IKMMLKYojyyNUQeE
ENV CLOUDINARY_CLOUD_NAME=daryn06r2
ENV DATABASE_URL=postgres://default:Utyxu15nKPEv@ep-dry-union-64351208-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

EXPOSE 8001