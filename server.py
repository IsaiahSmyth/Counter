from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret'


@app.route('/')
def index():
    if 'counter_num' in session:
        session['counter_num'] += 1
    else:
        session['counter_num'] = 0
    return render_template('index.html')




@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
