def lambda_handler(event, context):

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Glow Beauty</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#fff;
}

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 60px;
    background:white;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.logo{
    font-size:28px;
    font-weight:bold;
    color:#ff4f81;
}

.hero{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:70px 8%;
    background:linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb);
    flex-wrap:wrap;
}

.hero-text{
    width:50%;
    color:white;
}

.hero-text h1{
    font-size:58px;
    margin-bottom:15px;
}

.hero-text p{
    font-size:18px;
    line-height:1.6;
}

.btn{
    display:inline-block;
    margin-top:25px;
    padding:14px 28px;
    background:white;
    color:#ff4f81;
    text-decoration:none;
    border-radius:30px;
    font-weight:bold;
}

.hero-image{
    width:40%;
}

.hero-image img{
    width:100%;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

.products{
    padding:60px 8%;
    text-align:center;
}

.products h2{
    margin-bottom:40px;
    color:#ff4f81;
}

.cards{
    display:flex;
    gap:25px;
    justify-content:center;
    flex-wrap:wrap;
}

.card{
    width:260px;
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
}

.card img{
    width:100%;
    height:220px;
    object-fit:cover;
}

.card h3{
    padding-top:15px;
}

.card p{
    padding:10px;
}

.price{
    color:#ff4f81;
    font-weight:bold;
    padding-bottom:15px;
}

footer{
    text-align:center;
    padding:20px;
    background:#ff4f81;
    color:white;
}

@media(max-width:768px){

.hero{
    flex-direction:column;
    text-align:center;
}

.hero-text{
    width:100%;
}

.hero-image{
    width:100%;
    margin-top:30px;
}

}

</style>
</head>

<body>

<nav>
<div class="logo">Glow Beauty</div>
</nav>

<section class="hero">

<div class="hero-text">
<h1>Glow Naturally ✨</h1>

<p>
Premium skincare and cosmetic products designed
to keep your skin healthy, radiant and beautiful.
</p>

<a href="#" class="btn">Explore Products</a>
</div>

<div class="hero-image">
<img src="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=900&q=80">
</div>

</section>

<section class="products">

<h2>Featured Products</h2>

<div class="cards">

<div class="card">
<img src="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80">
<h3>Vitamin C Serum</h3>
<p>Brightens and refreshes your skin.</p>
<div class="price">₹799</div>
</div>

<div class="card">
<img src="https://images.unsplash.com/photo-1619451334792-150fd785ee74?auto=format&fit=crop&w=800&q=80">
<h3>Hydrating Cream</h3>
<p>Deep moisturization for every skin type.</p>
<div class="price">₹999</div>
</div>

<div class="card">
<img src="https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=800&q=80">
<h3>Sunscreen SPF 50</h3>
<p>Daily UV protection and skin care.</p>
<div class="price">₹699</div>
</div>

</div>

</section>

<footer>
© 2026 Glow Beauty | Premium Cosmetics
</footer>

</body>
</html>
"""

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    }
