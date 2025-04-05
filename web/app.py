import logging

from flask import Flask, render_template
from src.core import Kempfolds

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def kempfold():
    # return "<p>Hello, World!</p>"

    kemp = Kempfolds()
    kemp.return_kemps()
    kemp_image = kemp.get_random_kemp

    logger.info(f"kemp_image value: {kemp_image}")

    return render_template("index.html", url=kemp_image)
