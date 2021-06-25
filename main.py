import os
import time
import redis
from flask import Flask
from dotenv import load_dotenv
from dotenv import dotenv_values

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

load_dotenv()

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
app = Flask(__name__)

if os.getenv('config_env') == 'docker':
    cache = redis.Redis(host=config['redis_host'], port=os.getenv('redis_container_port'), password='1234qwer')
    conn_str = f'''mysql+mysqldb://root:1234qwer@{config["db_host"]}:3306/mlp?charset=utf8'''
else:
    # local
    cache = redis.Redis(host='127.0.0.1', port=16379, password='1234qwer')
    conn_str = f'''mysql+mysqldb://root:1234qwer@127.0.0.1:13306/mlp?charset=utf8'''

print(conn_str)
engine = create_engine(conn_str, poolclass=NullPool)



def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def get_index():
    count = get_hit_count()
    result = ''
    try:
        conn = engine.connect()
        rows = conn.execute("""SELECT * FROM icd where uid_icd=5;""")
        for row in rows:
            result = row
    except Exception as error:
        print(error)
    print('resulttttttttt=', result)
    return f'{result}<br><br><br><br><br><br><br><br><br><h1 style="color:#f67;font-size:100px">The {count} th visit!!!!!!!!</h1>'


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8888)