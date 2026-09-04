from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <main style="max-width:42rem;margin:5rem auto;font:18px system-ui;line-height:1.6">
      <h1>Flask is live on Render</h1>
      <p>This page was deployed automatically from GitHub.</p>
      <p><strong>Auto-deploy verified.</strong></p>
    </main>
    """


if __name__ == "__main__":
    app.run()
