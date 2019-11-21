import psycopg2

class ProdutoBanco:

def __init__(self):
    self.connection = psycopg2.connect(
        dbname = 'produto',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432')
