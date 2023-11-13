from flask import Flask
from view.animal_view import animal_blueprint
from view.recintos_view import recinto_blueprint

app = Flask(__name__)

app.register_blueprint(animal_blueprint)
app.register_blueprint(recinto_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
