from flask import Flask, render_template_string, session
import random

app = Flask(__name__)
app.secret_key = "super_secret_love_key"

her_name = "My Love"  # CHANGE THIS 💕

reasons = [
    "the way you make me feel calm just by existing",
    "how excited I get every time I hear from you",
    "your kindness, even in the smallest moments",
    "the way you make distance feel temporary",
    "how safe I feel being myself with you",
    "your laugh, which I replay in my head constantly",
    "the way you make me feel understood",
    "how you make my bad days better without trying",
    "the way loving you feels natural",
    "how you feel like home, even from far away",
]

random.shuffle(reasons)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Why I Love You 💖</title>
    <style>
        body {
            background: linear-gradient(135deg, #ffd6e8, #ffeef6);
            font-family: 'Georgia', serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            max-width: 420px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }

        h1 {
            color: #e75480;
            margin-bottom: 10px;
        }

        .reason-number {
            color: #999;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .reason {
            font-size: 18px;
            color: #444;
            margin-bottom: 30px;
            line-height: 1.5;
        }

        button {
            background-color: #e75480;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 30px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.1s ease, background-color 0.2s ease;
        }

        button:hover {
            background-color: #d64570;
            transform: scale(1.05);
        }

        footer {
            margin-top: 20px;
            font-size: 12px;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Why I Love You 💕</h1>
        <div class="reason-number">Reason #{{ number }}</div>
        <div class="reason">
            I love you because {{ reason }}.
        </div>
        <form method="post">
            <button type="submit">Press for another 💖</button>
        </form>
        <footer>Made with love, just for you</footer>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if "count" not in session:
        session["count"] = 0

    reason = reasons[session["count"] % len(reasons)]
    session["count"] += 1

    return render_template_string(
        HTML,
        reason=reason,
        number=session["count"]
    )

if __name__ == "__main__":
    app.run(debug=True)