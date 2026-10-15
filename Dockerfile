FROM python:3.11-slim

# Install system dependencies (ffmpeg is essential for audio extraction)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies first for Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Copy project files
COPY . .

# Render dynamically sets $PORT (usually 10000)
ENV PORT=10000
EXPOSE 10000

# Run Streamlit bound to Render's port and 0.0.0.0
CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT:-10000} --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false"]
