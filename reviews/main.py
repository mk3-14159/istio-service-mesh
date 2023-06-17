from fastapi import FastAPI


app = FastAPI(
    title='Reviews',
    description='This is reviews API',
    version='0.1.0'
)

reviews = [
    {'name': 'Raymond Melton', 'stars': 3, 'color-css': 'text-danger'},
    {'name': 'Kevin Dunn', 'stars': 1, 'color-css': 'text-danger'},
    {'name': 'Natasha Brown', 'stars': 5, 'color-css': 'text-danger'},
    {'name': 'Michelle Walker', 'stars': 4, 'color-css': 'text-danger'},
    {'name': 'Daniel Cooper', 'stars': 2, 'color-css': 'text-danger'},
]


@app.get("/reviews")
def get_all_reviews():
    return reviews
