from flask import Flask, render_template_string, session
import random

app = Flask(__name__)
app.secret_key = "super_secret_love_key"

her_name = "Varvara"  # CHANGE THIS 💕

reasons = [
    "you make me feel calm just by existing",
    "I get really excited every time I see a message from you popping up",
    "of your kindness, even when it is hard",
    "you make distance feel temporary",
    "I can feel safe being myself with you",
    "of your laugh, which I replay in my head constantly",
    "you make me feel understood",
    "you make my bad days better without trying",
    "the way loving you feels amazing",
    "you feel like home, even when I am far away from the Netherlands",
    "you smell like flowers",
    "everything you do makes me fall in love even more",
    "I am thinking of you every second of the day",
    "of your music taste",
    "you are so cool and I want to be as cool as you",
    "I feel loved for the first time",
    "I want to touch you (appropriately)",
    "I want to touch you (inappropriately)",
    "you make me want to give you all my money. Take it!!",
    "I care so deeply about you and want you to live your best life you could wish for",
    "you are the cutest, caring, kindest, bestest person alive",
    "I want you to be in every memory I will have from now on",
    "I feel the need to be the best version of myself",
    "I am probably wondering what you are doing as you read this",
    "you make me want to learn how to cook every single meal you desire",
    "of that cutie patootie face",
    "I am saving my money for when I will see you again",
    "I want to give you a big warm hug everytime you feel sad and tell you that everything is okay",
    "I never expected to create this for someone with so much love",
    "you make me look like a fool walking next to you",
    "people think I am the funniest person alive to have you as my girlfriend",
    "my heart skips a beat sometimes of excitement when I think of you",
    "everytime I close my eyes at night I dream of being with you",
    "I cannot wait to be living with you",
    "you have such a loving family and I feel part of it",
    "you have the most magical voice when you talk and sing I ever heard",
    "your curly hair is so so so pretty",
    "my heart melts when I think of your cuteness",
    "you make me feel supported in all the things I do and want to do",
    "you make every girl alive look like a goofball",
    "you changed my sexual orientation from heterosexual to Varvarasexual",
    "everyday I wish that I should have met you earlier",
    "made my exchange the best time of my life",
    "you are always cute, even when you are angry, cry, happy, neutral",
    "I want to know what you are doing every single second of the day",
    "I think of our first date a lot :)",
    "you have the most contagious smile ever",
    "you gave me a chance :0 I still don't know how I got the chance",
    "you deserve all the love and kindness in the world",
    "you can calm me down really quick when I am anxious",
    "your passion for psychology is really cool and I love talking about it with you",
    "you dress really well",
    "you make me want to be a better person by putting myself in uncomfortable situations",
    "I get shy talking with you sometimes",
    "you’re gentle with my feelings, even when I’m not great at expressing them",
    "you make deep conversations feel natural and easy",
    "you bring a sense of calm into my life",
    "you’re emotionally intelligent in a way I really admire",
    "you make me want to open up more",
    "I smile at my screen and get called out for it sometimes",
    "I get jealous when you talk to other people :(",
    "I like imagining what it will be like when we are together in person",
    "you distract me from negative thoughts",
    "I look at photos of you when I feel lonely",
    "I feel special knowing I get to talk and spend time with you",
    "I get a little proud when I make you laugh",
    "I get shy when you compliment me and I don't know how to react",
    "I like knowing I’m part of your little world",
    "I think of you when certain songs come up",
    "the music you share with me is really nice and I think of you when I listen to it ",
    "you make me feel like I am a little kid again when I am with you",
    "you look hot playing the bass and also when you sing but I didn't see that yet :(",
    "you look really cute walking around and having your mini sprints",
    "I could go on forever with listing reasons why I love you",
    "I find it cute that you always used to pick the same drink at the convenience store",
    "you make me want to workout all days of the week",
    "you make me feel cared for on a level I didn't know existed",
    "you remind me of a cute kitten when I see your face",
    "you make me want to find a cure for your period cramps",
    "you made me code this and trained my patience :)",
    "you could lock me up in a basement and only let me see you and I would still be the happiest person alive",
    "I want to waste my time only with you really",
    "you make me believe there's something more than life",
    "you make me feel like I have completed life already",
    "I never cared so much about someone's feelings",
    "you make me show my romantic side which I didn't knew I had",
    "whoever you dislike, I dislike too :)",
    "you make me create this while I have to study instead but I will catch up on less important stuff later",
    "I can't imagine a future where you aren't part of",
    "I just want to be with you 24/7",
    "you giving compliments is the best feeling in the world",
    "I never cared so much about what to gift you for anniversaries",
    "you make me want to learn taekwondo to protect you",
    "you make me want to study how to produce music to help you with your singing",
    "I want to learn Ukrainian/Russian to communicate with you",
    "I want to play with you in a band",
    "I never asked for someone perfect but I still got you",
    "I want to hear every single detail of your day",
    "your voice alone sounds like magic and makes me feel warm",
    "I love it when you make that sad face when I say I have to go :( It makes me want to stay longer",
    "I want to show you all my childhood spots in my hometown",
    "you can tolerate spicy food and it's cool. I want to be like you",
    "I love talking about how amazing you are to other people",
    "all your presents you give me mean so much to me",
    "I keep wondering why I deserve you",
    "you make me want research your interests so that I can talk about it with you",
    "you make it easier for me to get out of bed knowing that I'm your boyfriend :0",
    "I got into jazz more since we went to that jazz bar and it's really nice",
    "you want a future with me??? ME TOO!!!",
    "you listen to my random facts and that means a lot to me",
    "you make me feel like everything will be okay",
    "I look at the photos of yourself you send me everyday. Yes everyday",
    "you are the only person I would give my last sushi piece to",
    "you increase my screen time and it doesn't feel like I'm wasting my time whatsoever",
    "you are the only person that could steal all my clothes",
    "you make me want to brag about you to strangers",
    "I always check my reflection before video calls",
    "you are genuinely funny and you make me laugh so easily",
    "you make me want to remember every single thing you say",
    "you make me want to check my phone even when it didn’t buzz, just to be sure that I didn't miss a message from you",
    "I can't stop thinking about how it would feel like to go home after a rough day and you being there",
    "you make daydreaming not boring anymore :)",
    "I see the whole world when I look at you",
    "I love hearing your gossip it's really fun",
    "you make me want to remember every detail of your face",
    "I feel like I can't express my love anymore to you. It is too big",
    "you make me feel warm and comfortable even on facetime",
    "I look forward to your good morning and goodnight messages",
    "you make me write these reasons past midnight because I miss you so much",
    "cuddling with you for a full day and nothing else is in my eyes a perfect day",
    "listening to your childhood memories is so fun and I want to know more about it",
    "I keep scrolling Instagram reels to look for the ones you liked",
    "I always get a little happier knowing your part of my life",
    "of how easy it is to talk to you for hours",
    "I get excited when I get the chance to yap about my day to you",
    "I feel connected to you in a way that feels real",
    "I wonder what's going inside your head that makes you so amazing",
    "your smile makes me want to lock you up and keep you somewhere no one else sees you :)",
    "you know me better than everyone else right now",
]

random.shuffle(reasons)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Why I Love You Varvara 💖</title>
    <style>
        body {
            background: linear-gradient(135deg, #ffd6e8, #ffeef6);
            font-family: 'Georgia', serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 10px;
            overflow: hidden; /* Needed for floating hearts */
        }

        /* ✨ FLOATING HEARTS BACKGROUND ✨ */
        .hearts {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 0;
        }

        .heart {
            position: absolute;
            bottom: -50px;
            font-size: 20px;
            opacity: 0.6;
            animation: floatUp 6s linear infinite;
        }

        @keyframes floatUp {
            0% {
                transform: translateY(0) translateX(0) scale(1);
                opacity: 0.6;
            }
            100% {
                transform: translateY(-120vh) translateX(20px) scale(1.4);
                opacity: 0;
            }
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            max-width: 420px;
            width: 100%;
            text-align: center;
            box-shadow: 
                0 20px 40px rgba(0,0,0,0.1),
                0 0 25px rgba(231, 84, 128, 0.25);
            transition: opacity 0.3s ease;
            z-index: 2; /* Above hearts */
            position: relative;
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

        /* PHONE VERSION */
        @media (max-width: 480px) {
            .card {
                padding: 20px;
                max-width: 90%;
            }

            h1 {
                font-size: 22px;
            }

            .reason {
                font-size: 16px;
            }

            button {
                width: 100%;
                padding: 14px;
                font-size: 16px;
            }
        }
    </style>
</head>
<body>

    <!-- ✨ Floating hearts container -->
    <div class="hearts" id="hearts"></div>

    <div class="card" id="card">
        <h1>Why I Love You Varvara 💕</h1>
        <div class="reason-number">Reason #{{ number }}</div>
        <div class="reason">
            I love you because {{ reason }}.
        </div>

        <button id="next-btn">Press for another 💖</button>

        <footer>Made with love, just for you</footer>
        <footer>November 1st, 2025 💗</footer>
    </div>

    <script>
    /* ✨ Generate floating hearts continuously ✨ */
    function createHeart() {
        const hearts = document.getElementById("hearts");
        const heart = document.createElement("div");
        heart.classList.add("heart");
        heart.innerHTML = "💖";

        // Random horizontal position
        heart.style.left = Math.random() * 100 + "vw";

        // Random animation duration
        heart.style.animationDuration = (5 + Math.random() * 3) + "s";

        hearts.appendChild(heart);

        // Remove heart after animation
        setTimeout(() => heart.remove(), 8000);
    }

    setInterval(createHeart, 800);

    /* ✨ Button logic with typing effect ✨ */
    document.getElementById("next-btn").addEventListener("click", async () => {
        const reasonBox = document.querySelector(".reason");
        const numberBox = document.querySelector(".reason-number");

        reasonBox.style.opacity = "0";
        numberBox.style.opacity = "0";

        setTimeout(() => {
            reasonBox.innerHTML = "🤔";
            numberBox.innerHTML = "";
            reasonBox.style.opacity = "1";
        }, 150);

        await new Promise(resolve => setTimeout(resolve, 500));

        const response = await fetch("/next", { method: "POST" });
        const data = await response.json();

        reasonBox.style.opacity = "0";

        function typeText(element, text, speed = 25) {
            element.innerHTML = "";
            let i = 0;
            let interval = setInterval(() => {
                element.innerHTML += text[i];
                i++;
                if (i >= text.length) clearInterval(interval);
            }, speed);
        }

        setTimeout(() => {
            numberBox.innerHTML = "Reason #" + data.number;
            numberBox.style.opacity = "1";

            const fullText = "I love you because " + data.reason + ".";
            typeText(reasonBox, fullText);

            reasonBox.style.opacity = "1";
        }, 200);
    });
    </script>

</body>
</html>
"""


@app.route("/", methods=["GET"])
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

@app.route("/next", methods=["POST"])
def next_reason():
    if "count" not in session:
        session["count"] = 0

    reason = reasons[session["count"] % len(reasons)]
    session["count"] += 1

    return {"reason": reason, "number": session["count"]}

if __name__ == "__main__":
    app.run(debug=True)
