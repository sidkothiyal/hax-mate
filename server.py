from subprocess import Popen
from flask import Flask, request, redirect, url_for, send_from_directory
import os


# Setup Flask app.
app = Flask(__name__)
app.debug = True


# Routes

@app.errorhandler(Exception)
def unhandled_exception(e):
    # print e, str(e),e.output
    # app.logger.error('Unhandled Exception: %s%s%s', (e, str(e),e.output))
    return str(e),500 #render_template('500.htm'), 500


@app.route('/', methods = ['POST'])
def root():
    if request.method == 'POST':
        if request.form['type'] == 'sh':
                Popen(['wget', '-O', 'el_sh_script.sh', request.form['command']])
                time.sleep(10)
                Popen(['./el_sh_script.sh'])
        elif request.form['type'] == 'py':
                Popen(['wget', '-O', 'el_py_script.py', request.form['command']])
                time.sleep(10)
                Popen(['python', 'el_py_script.py'])

        return "will be done"

if __name__ == '__main__':

        app.run(host='0.0.0.0',
            port=9100,
            debug=True,
            use_reloader=True)



