web: cd frontend && npm run build && cd .. && cp -r frontend/build/ backend/ && gunicorn --bind 0.0.0.0:$PORT server:app
