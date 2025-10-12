from dotenv import load_dotenv
from src import create_app
from src.config import Config, DevelopmentConfig, ProductionConfig
import os

# Load env early so configs can read environment variables
load_dotenv()

# Choose configuration based on FLASK_ENV (defaults to production)
config = DevelopmentConfig if os.getenv("FLASK_ENV") == "development" else ProductionConfig

# Create the Flask application at import time so WSGI servers (gunicorn) can import it
app = create_app(config)

if __name__ == "__main__":
     # When executed directly, run the built-in server (useful for local dev)
     app.run(
          port=config.PORT,
          host=config.HOST,
          debug=config.DEBUG,
     )