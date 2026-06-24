FROM python:3.11-slim
WORKDIR /jogo-da-vida

COPY . .
CMD ["sh", "-c", "python jogo-da-vida.py < entradas.txt"]