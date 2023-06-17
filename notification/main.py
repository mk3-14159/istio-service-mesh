from fastapi import FastAPI


app = FastAPI(
    title='Notifications',
    description='This is notification API',
    version='0.1.0'
)

notifications = [
    {'name': 'Raymond Melton', 'message': 'Fight and road more hard whose.'},
    {'name': 'Kevin Dunn', 'message': 'Ten environmental soldier often.'},
    {'name': 'Natasha Brown', 'message': 'Society for under three every.'},
    {'name': 'Michelle Walker', 'message': 'Him bar body speak city site person.'},
    {'name': 'Daniel Cooper', 'message': 'Better south resource.'},
]


@app.get("/notifications")
def get_all_notifications():
    return notifications
