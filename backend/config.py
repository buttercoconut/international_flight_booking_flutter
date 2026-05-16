# Configuration for the backend service
# You can extend this file to include database URLs, secret keys, etc.

DATABASE_URL = "postgresql://user:password@localhost:5432/flightdb"
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
