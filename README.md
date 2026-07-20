Simple Chatbot

This minimal chatbot runs a Flask server and supports:
- Telling jokes (type: "tell me a joke")
- Calculations (e.g. `2+2`, `sqrt(16)`) via a safe local evaluator
- Problem-solving using OpenAI if `OPENAI_API_KEY` is set; otherwise a local fallback

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Optionally set your OpenAI key:
# $env:OPENAI_API_KEY = 'sk-...'
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Notes:
- The app uses a safe AST-based evaluator for arithmetic and a small set of math functions.
- If you set `OPENAI_API_KEY`, the app will attempt to use the OpenAI Chat API for general "solve" requests.
- Improve intents and add more jokes or knowledge sources as next steps.

Deployment (make the app live 24/7)

1) Quick container build (local test):

```powershell
docker build -t chatbot .
docker run -p 5000:5000 chatbot
```

2) Deploy to a cloud host (recommended)

- Option A — Render: connect this repository to Render, choose "Web Service", select Docker, and point the service to use the image built from the repo. Render will run the container 24/7 and provide a public URL.

- Option B — Fly.io: install `flyctl`, run `fly launch`, and deploy the Dockerfile. Fly provides a stable public URL and automatic restarts.

- Option C — Railway / Railway.app: connect repo and deploy using Docker or their Node/Python buildpacks.

3) Using GitHub Container Registry

The included GitHub Actions workflow `/.github/workflows/build-and-push.yml` builds and pushes an image to GitHub Container Registry (`ghcr.io/<owner>/<repo>:latest`) when you push to `main`/`master`. You can then configure your cloud host to pull that image.

Provider-specific configs included:

- `render.yaml` — configuration for Render (Docker-based Web Service). Connect your GitHub repo to Render and it will build and run this service.
- `fly.toml` — configuration for Fly.io. Use `fly launch` (or `fly deploy`) to create an app and deploy using this file.

Provider deployment steps (concise):

- Render
  1. Sign in to Render and connect your GitHub account.
  2. Create a new "Web Service" and choose this repository.
  3. Select "Docker" as the environment; Render will build the Dockerfile and run the container.
  4. Add the secret `OPENAI_API_KEY` in Render's environment settings if you want cloud answers.

- Fly.io
  1. Install `flyctl`: https://fly.io/docs/hands-on/install-flyctl/
  2. Run `flyctl launch` in the repo; choose the `fly.toml` app name or accept the generated one.
  3. Set the secret: `flyctl secrets set OPENAI_API_KEY=<your_key>`
  4. Deploy: `flyctl deploy`

Notes on access and next steps:
- I can perform the deploy for you if you connect your GitHub account to the chosen provider (recommended) or provide a deploy key/API token. For security, prefer connecting GitHub rather than sharing raw credentials.
- Tell me which provider you prefer and whether you'd like me to proceed with a full deploy (you'll be asked to authorize third-party access during the provider flow).

