from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>WalkwithShubh</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, sans-serif;
        }

        body{
            background:#f5f5f5;
        }

        nav{
            background:#0d6efd;
            color:white;
            padding:15px 50px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        nav h1{
            font-size:28px;
        }

        nav ul{
            display:flex;
            list-style:none;
        }

        nav ul li{
            margin-left:20px;
        }

        nav ul li a{
            color:white;
            text-decoration:none;
        }

        .hero{
            height:70vh;
            background:url('https://images.unsplash.com/photo-1524492412937-b28074a5d7da') center/cover;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            color:white;
            text-align:center;
        }

        .hero h2{
            font-size:50px;
            margin-bottom:15px;
        }

        .hero p{
            font-size:20px;
            margin-bottom:20px;
        }

        .search-box{
            padding:12px;
            width:300px;
            border:none;
            border-radius:5px;
        }

        .section-title{
            text-align:center;
            margin:40px 0;
            font-size:35px;
        }

        .places{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
            gap:25px;
            padding:30px;
        }

        .card{
            background:white;
            border-radius:10px;
            overflow:hidden;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        }

        .card img{
            width:100%;
            height:220px;
            object-fit:cover;
        }

        .card h3{
            padding:15px;
        }

        .card p{
            padding:0 15px 15px;
        }

        .about{
            padding:60px;
            text-align:center;
            background:white;
        }

        .contact{
            padding:60px;
            text-align:center;
        }

        .contact input,
        .contact textarea{
            width:60%;
            padding:12px;
            margin:10px;
        }

        .contact button{
            background:#0d6efd;
            color:white;
            border:none;
            padding:12px 25px;
            cursor:pointer;
        }

        footer{
            background:#222;
            color:white;
            text-align:center;
            padding:20px;
        }

    </style>

</head>

<body>

<nav>
    <h1>WalkwithShubh</h1>

    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Destinations</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

<section class="hero">

    <h2>Explore Incredible India</h2>

    <p>Discover the most beautiful places in India</p>

    <input class="search-box" type="text" placeholder="Search destinations...">

</section>

<h2 class="section-title">Top Tourist Places</h2>

<section class="places">

<div class="card">
<img src="https://images.pexels.com/photos/28762052/pexels-photo-28762052/free-photo-of-taj-mahal-with-tourists-and-clear-sky.jpeg?auto=compress&cs=tinysrgb&w=1600">
<h3>Taj Mahal</h3>
<p>Agra, Uttar Pradesh</p>
</div>

<div class="card">
<img src="https://media.istockphoto.com/id/1744632361/photo/city-palace-jaipur-india.webp?a=1&b=1&s=612x612&w=0&k=20&c=C3QEihz-Rl0mUJrMGow6ZLUdRurLRUihz6q1eSHoPjM=">
<h3>Jaipur</h3>
<p>Pink City of Rajasthan</p>
</div>

<div class="card">
<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/df26146d-a16d-4d75-8172-aa1d9c984001/d6omi5n-98f44af3-fc69-49c3-968d-065d355f565e.jpg/v1/fill/w_900,h_600,q_75,strp/varanasi___india_by_rezaphotography_d6omi5n-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjAwIiwicGF0aCI6IlwvZlwvZGYyNjE0NmQtYTE2ZC00ZDc1LTgxNzItYWExZDljOTg0MDAxXC9kNm9taTVuLTk4ZjQ0YWYzLWZjNjktNDljMy05NjhkLTA2NWQzNTVmNTY1ZS5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.C0csHsx1aB5YrFqjylvIfLO6qihzqjiCXccfchR9bMc">
<h3>Varanasi</h3>
<p>Spiritual Capital of India</p>
</div>

<div class="card">
<img src="https://wildlifezones.com/wp-content/uploads/2020/10/A-Beautiful-Beach-in-Goa.jpg">
<h3>Goa</h3>
<p>Famous Beaches & Nightlife</p>
</div>

<div class="card">
<img src="https://www.affordableluxurytravel.co.uk/blog/wp-content/uploads/2023/03/Kerala-Backwaters-2.jpg">
<h3>Kerala</h3>
<p>Beautiful Backwaters</p>
</div>

<div class="card">
<img src="https://wallpapers.com/images/hd/golden-temple-and-green-pool-yeah6u7p3v71u682.jpg">
<h3>Golden Temple</h3>
<p>Amritsar, Punjab</p>
</div>

<div class="card">
<img src="https://cdn.guidetour.in/wp-content/uploads/2018/09/Architectural-Marvel-Gateway-of-India.jpg.webp">
<h3>Mumbai</h3>
<p>Gateway of India</p>
</div>

<div class="card">
<img src="https://imgmedia.lbb.in/media/2019/09/5d6e3d3631019eb679a4639d_1567505718634.jpg">
<h3>Qutub Minar</h3>
<p>Delhi</p>
</div>

<div class="card">
<img src="https://wanderon-images.gumlet.io/blogs/new/2023/12/leh-ladakh.jpg">
<h3>Leh Ladakh</h3>
<p>Adventure Paradise</p>
</div>

<div class="card">
<img src="https://www.fabhotels.com/blog/wp-content/uploads/2019/05/Mysore-palace_600.jpg">
<h3>Mysore Palace</h3>
<p>Karnataka</p>
</div>

</section>

<section class="about">

<h2>About WalkwithShubh</h2>

<br>

<p>
WalkwithShubh helps travelers discover India's most iconic destinations.
Explore culture, history, spirituality and adventure all in one place.
</p>

<div class="card">
<img src="/static/myphoto.jpg.jpg" 
    alt="Shubham Gupta"
    style="width:250px;border-radius:15px;">
<h3>Shubham Gupta</h3>
<p>Founder</p>
</div>

</section>

<section class="contact">

<h2>Contact Us</h2>

<br>

<input type="text" placeholder="Your Name"><br>

<input type="email" placeholder="Your Email"><br>

<textarea rows="5" placeholder="Message"></textarea><br>

<button>Send Message</button>

</section>

<footer>

<h3>© 2026 WalkwithShubh | Made by Shubham</h3>

</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
    
