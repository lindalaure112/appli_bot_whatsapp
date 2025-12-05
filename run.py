from flask import Flask
from app import create_app, db
from flask_migrate import Migrate
from app.utils.scheduler import demarrer_planificateur


app = create_app()
demarrer_planificateur()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)