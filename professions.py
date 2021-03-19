from flask import Flask, request, url_for, render_template
app = Flask(__name__)


@app.route('/list_prof/<prof>')
def index(prof):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html',  
                           type=prof)
  
  
if __name__ == "__main__":
    app.run(port=8080, debug=True)
