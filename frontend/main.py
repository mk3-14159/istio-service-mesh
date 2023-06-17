import os
import logging
import requests

from flask import Flask, render_template, request


app = Flask(__name__)

NOTIFICATION_SERVICE_ENDPOINT = os.getenv('NOTIFICATION_SERVICE_ENDPOINT', 'localhost')
NOTIFICATION_SERVICE_PORT = os.getenv('NOTIFICATION_SERVICE_PORT', '8001')

DETAILS_SERVICE_ENDPOINT = os.getenv('DETAILS_SERVICE_ENDPOINT', 'localhost')
DETAILS_SERVICE_PORT = os.getenv('DETAILS_SERVICE_PORT', '8002')

PERFORMANCE_SERVICE_ENDPOINT = os.getenv('PERFORMANCE_SERVICE_ENDPOINT', 'localhost')
PERFORMANCE_SERVICE_PORT = os.getenv('PERFORMANCE_SERVICE_PORT', '8003')

REVIEWS_SERVICE_ENDPOINT = os.getenv('REVIEWS_SERVICE_ENDPOINT', 'localhost')
REVIEWS_SERVICE_PORT = os.getenv('REVIEWS_SERVICE_PORT', '8004')


# logger config
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[logging.FileHandler('debug.log'), logging.StreamHandler()],
)


@app.route("/")
@app.route("/home")
@app.route("/employees")
def home_page():
    position = request.headers.get('position')
    notification_response = requests.get(
        ('http://{0}:{1}/notifications').format(NOTIFICATION_SERVICE_ENDPOINT, NOTIFICATION_SERVICE_PORT)
    )

    details_response = requests.get(
        ('http://{0}:{1}/details').format(DETAILS_SERVICE_ENDPOINT, DETAILS_SERVICE_PORT)
    )

    reviews_response = requests.get(
        ('http://{0}:{1}/reviews').format(REVIEWS_SERVICE_ENDPOINT, REVIEWS_SERVICE_PORT)
    )

    performance_response = None
    if position:
        if position.lower() in ['manager', 'director', 'ceo']:
            performance_response = requests.get(
                ('http://{0}:{1}/performances').format(PERFORMANCE_SERVICE_ENDPOINT, PERFORMANCE_SERVICE_PORT),
                headers={'position': position}
            )

    return render_template(
        "index.html",
        notifications=notification_response.json(),
        details=details_response.json(),
        performances=performance_response,
        reviews=reviews_response.json(),
        eligible_to_view_performance=True if performance_response else False,
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)