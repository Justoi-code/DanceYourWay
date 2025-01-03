from app import create_app
import os
from dotenv import load_dotenv

app = create_app()

# Get port from environment variable or default to 5000
port = int(os.getenv("FLASK_PORT", 5000))

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_ENV") == "development", host="0.0.0.0", port=port)