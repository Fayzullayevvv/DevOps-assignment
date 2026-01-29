from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
# Topshiriq 7: Mahsulot yangilanishlarini sanaydigan custom metric 
UPDATE_METRIC = Counter('agri_product_updates_total', 'Total farm product updates')

@app.route('/update')
def update():
    UPDATE_METRIC.inc()
    return "Product Updated!"

if __name__ == '__main__':
    start_http_server(8000) # Metrikalar uchun port
    app.run(host='0.0.0.0', port=5000)