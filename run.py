from flask import Flask

from config import Config

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import parts of our application
        from controller import routes
        from scheduler import init_scheduler

        # Initialize the scheduler
        if(Config.SCHEDULER_ENABLED == 'true'):
            init_scheduler()

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5132)