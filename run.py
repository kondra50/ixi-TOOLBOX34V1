from waitress import serve
from app import app


if __name__ == "__main__":
  serve(app, port=8091 , url_scheme='https')
