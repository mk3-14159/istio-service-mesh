from fastapi import FastAPI, Request


app = FastAPI(
    title='Performances',
    description='This is performance API',
    version='0.1.0'
)

performances = [
    {'id': 1, 'name': 'Michael Greene', 'performance_feedback': 'Human too us candidate risk.'},
    {'id': 2, 'name': 'Michael Williams', 'performance_feedback': 'Generation voice move your work week hundred wish.'},
    {'id': 3, 'name': 'Carlos Miller', 'performance_feedback': 'Again do always night paper.'},
    {'id': 4, 'name': 'Lindsay Herrera', 'performance_feedback': 'Maybe where already meeting left least.'},
    {'id': 5, 'name': 'John Schultz', 'performance_feedback': 'Effect decade industry business save feel brother.'},
    {'id': 6, 'name': 'Robert Hayes', 'performance_feedback': 'Third raise west indicate listen sometimes news less.'},
    {'id': 7, 'name': 'Harold Gray', 'performance_feedback': 'Million attack between paper cover.'},
    {'id': 8, 'name': 'Kenneth Howard', 'performance_feedback': 'Probably new class.'},
    {'id': 9, 'name': 'Heather May', 'performance_feedback': 'Hand hospital or prepare recently paper north.'},
    {'id': 10, 'name': 'Steven Taylor', 'performance_feedback': 'No series require about food.'},
]


@app.get("/performances")
def get_all_performances(request: Request):
    return performances
    # position = request.headers.get('position')
    # if position:
    #     if position.lower() in ['manager', 'director', 'ceo']:
    #         return performances
    #     else:
    #         return {'message': 'You are not eligible to view the employee performance'}
    # else:
    #     return {'message': 'Please fill in your position in headers'}
