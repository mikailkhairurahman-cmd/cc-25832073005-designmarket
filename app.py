
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

APP_NAME = "DesignMarket"
APP_VERSION = "0.1.0"
APP_ENV = os.getenv("APP_ENV", "development")

# Data contoh layanan marketplace untuk M03
LAYANAN_DESAIN = [
    {
        "nama": "Desain Logo",
        "kategori": "Branding",
        "harga": 50000,
        "desainer": "Creative Studio"
    },
    {
        "nama": "Desain Poster",
        "kategori": "Promosi",
        "harga": 30000,
        "desainer": "Visual Art"
    },
    {
        "nama": "Desain Banner",
        "kategori": "Marketing",
        "harga": 40000,
        "desainer": "Pixel Design"
    },
    {
        "nama": "Desain Konten Instagram",
        "kategori": "Media Sosial",
        "harga": 25000,
        "desainer": "Social Creative"
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        layanan=LAYANAN_DESAIN
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
        "description": "Marketplace Jasa Desain",
        "total_layanan": len(LAYANAN_DESAIN)
    }), 200


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
