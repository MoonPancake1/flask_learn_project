from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная'
@app.route('/news')
def news():
    return 'Новости'
@app.route('/news_detail/<int:id>')
def news_detail(id: int):
    return f'Новость {id}'


if __name__ == '__main__':
    app.run(debug=True)