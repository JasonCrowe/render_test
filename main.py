from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Render Test</title>
        <style>
          * { box-sizing: border-box; }
          body {
            margin: 0;
            color: #171717;
            background: #fff;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
          }
          body::before {
            position: fixed;
            inset: 0;
            z-index: -1;
            content: "";
            background:
              radial-gradient(circle at 20% 0%, #e9f4ff 0, transparent 32rem),
              radial-gradient(circle at 80% 8%, #f5eaff 0, transparent 28rem);
          }
          main { width: min(1100px, calc(100% - 40px)); margin: auto; }
          nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 72px;
            font-size: 14px;
          }
          .brand { display: flex; align-items: center; gap: 10px; font-weight: 650; }
          .mark { width: 0; height: 0; border-right: 9px solid transparent; border-bottom: 16px solid #171717; border-left: 9px solid transparent; }
          .status {
            padding: 7px 11px;
            color: #08783e;
            background: #eafaf1;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 600;
          }
          .status::before { content: ""; display: inline-block; width: 7px; height: 7px; margin-right: 7px; background: #22c55e; border-radius: 50%; }
          .hero { max-width: 780px; padding: 110px 0 90px; }
          .eyebrow { margin: 0 0 22px; color: #666; font: 500 12px ui-monospace, monospace; letter-spacing: .12em; text-transform: uppercase; }
          h1 { margin: 0; font-size: clamp(48px, 8vw, 82px); line-height: .98; letter-spacing: -.065em; }
          .lead { max-width: 640px; margin: 30px 0 0; color: #555; font-size: clamp(18px, 2.3vw, 22px); line-height: 1.6; }
          .grid { display: grid; grid-template-columns: repeat(3, 1fr); margin-bottom: 70px; border-radius: 14px; box-shadow: 0 0 0 1px rgb(0 0 0 / 8%), 0 18px 45px -30px rgb(0 0 0 / 35%); overflow: hidden; }
          .card { min-height: 220px; padding: 30px; background: rgb(255 255 255 / 75%); backdrop-filter: blur(12px); }
          .card + .card { box-shadow: -1px 0 rgb(0 0 0 / 8%); }
          .number { color: #888; font: 500 12px ui-monospace, monospace; }
          h2 { margin: 50px 0 10px; font-size: 22px; letter-spacing: -.035em; }
          .card p { margin: 0; color: #666; line-height: 1.55; }
          footer { padding: 24px 0 40px; color: #888; font-size: 13px; box-shadow: 0 -1px rgb(0 0 0 / 8%); }
          @media (max-width: 700px) {
            .hero { padding: 80px 0 65px; }
            .grid { grid-template-columns: 1fr; }
            .card { min-height: 180px; }
            .card + .card { box-shadow: 0 -1px rgb(0 0 0 / 8%); }
            h2 { margin-top: 35px; }
          }
        </style>
      </head>
      <body>
        <main>
          <nav>
            <div class="brand"><span class="mark"></span> Render Test</div>
            <div class="status">Live</div>
          </nav>
          <section class="hero">
            <p class="eyebrow">Git push → Render deploy</p>
            <h1>Ship code.<br>Skip the chores.</h1>
            <p class="lead">A tiny Flask app proving that every push to GitHub can become a live deployment—automatically.</p>
          </section>
          <section class="grid" aria-label="Deployment flow">
            <article class="card"><span class="number">01</span><h2>Build</h2><p>Keep the app small, clear, and easy to change.</p></article>
            <article class="card"><span class="number">02</span><h2>Push</h2><p>GitHub receives the new revision on the main branch.</p></article>
            <article class="card"><span class="number">03</span><h2>Deploy</h2><p>Render publishes the update on its free web tier.</p></article>
          </section>
          <footer>Flask · GitHub Actions · Render</footer>
        </main>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
