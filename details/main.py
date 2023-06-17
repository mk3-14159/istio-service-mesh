from fastapi import FastAPI, status, HTTPException


app = FastAPI(
    title='Details',
    description='This is details API',
    version='0.1.0'
)

details = [
    {'id': 1, 'name': 'Michael Greene', 'email': 'stephanieolson@example.org', 'country': 'Solomon Islands'},
    {'id': 2, 'name': 'Michael Williams', 'email': 'floyddaisy@example.com', 'country': 'Monaco'},
    {'id': 3, 'name': 'Carlos Miller', 'email': 'jaimeanderson@example.org', 'country': 'Taiwan'},
    {'id': 4, 'name': 'Lindsay Herrera', 'email': 'joneskari@example.com', 'country': 'Barbados'},
    {'id': 5, 'name': 'John Schultz', 'email': 'yorozco@example.org', 'country': 'Aruba'},
    {'id': 6, 'name': 'Robert Hayes', 'email': 'carolrodriguez@example.com', 'country': 'Indonesia'},
    {'id': 7, 'name': 'Harold Gray', 'email': 'aguilargary@example.org', 'country': 'Somalia'},
    {'id': 8, 'name': 'Kenneth Howard', 'email': 'mccalljohn@example.net', 'country': 'United Arab Emirates'},
    {'id': 9, 'name': 'Heather May', 'email': 'victoria04@example.org', 'country': 'Saint Martin'},
    {'id': 10, 'name': 'Steven Taylor', 'email': 'kshaw@example.org', 'country': 'Saint Martin'},
]


@app.get("/details")
def get_all_details():
    return details


@app.get("/details/{id}")
def get_detail(id: int):
    detail = None

    for d in details:
        if d['id'] == id:
            detail = d
            break
    if not detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Detail with id: {id} was not found'
        )
    return detail
