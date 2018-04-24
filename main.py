import os

from flask_migrate import Migrate

from Graduate_work import create_app, db
from Graduate_work.models import Classifier, Set, Task
from Graduate_work.database import init_db
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'rahasiabesar'

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Classifier=Classifier, Set=Set, Task=Task)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    app.run(debug=True)
