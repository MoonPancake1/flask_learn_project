from flask import Flask, url_for


def is_prime(n: int) -> bool:
    for i in range(2, int(n**.5)+1):
        if not n % i:
            return False
    return True


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
@app.route('/primes/<int:n>')
def prime(n: int):
    answ, i = [], 2
    while len(answ) != n:
        if is_prime(i):
            answ.append(i)
        i += 1
    return f'{" ".join(list(map(str, answ)))}'


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/post/<int:id>')
# def post(id):
#     pass


# with app.test_request_context():
#     print(url_for('post', id=12))