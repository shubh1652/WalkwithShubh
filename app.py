from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WalkwithShubh</title>

    <style>
        body{
            margin:0;
            font-family:Arial, sans-serif;
            background:#f4f4f4;
        }

        nav{
            background:#1e3a8a;
            color:white;
            padding:15px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .logo{
            font-size:28px;
            font-weight:bold;
        }

        ul{
            list-style:none;
            display:flex;
            gap:20px;
        }

        ul li a{
            color:white;
            text-decoration:none;
        }

        .hero{
            text-align:center;
            padding:80px 20px;
            background:url('https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1200') center/cover;
            color:white;
        }

        .hero h1{
            font-size:50px;
        }

        .about{
            padding:50px;
            text-align:center;
            background:white;
        }

        .about img{
            width:220px;
            border-radius:50%;
            margin-top:20px;
        }
    </style>
</head>
<body>

<nav>
    <div class="logo">WalkwithShubh ✈</div>

    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Destinations</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

<section class="hero">
    <h1>Explore Incredible India</h1>
    <p>Discover India's most beautiful tourist destinations.</p>
</section>

<section class="about">
    <h2>About WalkwithShubh</h2>

    <p>
        WalkwithShubh helps travelers discover India's most iconic destinations.
        Explore culture, history, spirituality and adventure all in one place.
    </p>

    <img src="/static/myphoto.jpg.jpg" alt="Shubham">

    <h3>Shubham Gupta</h3>
    <p>Founder</p>
</section>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
