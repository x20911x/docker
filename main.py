import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='127.0.0.1', port=16379, password='1234qwer')


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
    return f'<br><br><br><br><br><br><br><br><br><h1 style="color:#f67;font-size:100px">The {count} time visit!!!!!!!!</h1>'


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8888)