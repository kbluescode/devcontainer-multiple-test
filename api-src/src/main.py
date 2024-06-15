from flask import Flask, g
from redis import Redis
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = Redis(host='redis', port=6379)
    return db

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get/<string:key>")
def get_redis_key(key: str):
    db = get_db()
    try:
        result = db.get(key)
        return { 'value': result.decode('utf-8') }
    except:
        return { 'error': f'Failed getting {key}' }

@app.route("/set/<string:key>/<string:value>")
def set_redis_key(key: str, value: str):
    db = get_db()
    try:
        result = db.set(key, value)
        return f'Result: {result}'
    except:
        return f'Failed setting: {key}={value}'