def lambda_handler(event, context):

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AWS Quiz App</title>

<style>
body{
    font-family:Arial,sans-serif;
    background:linear-gradient(135deg,#667eea,#764ba2);
    padding:30px;
}

.container{
    max-width:800px;
    margin:auto;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 5px 20px rgba(0,0,0,0.2);
}

h1{
    text-align:center;
    color:#764ba2;
}

.question{
    margin-top:25px;
}

button{
    margin-top:25px;
    padding:12px 25px;
    border:none;
    background:#764ba2;
    color:white;
    border-radius:8px;
    cursor:pointer;
}

#result{
    margin-top:25px;
    font-size:22px;
    font-weight:bold;
}
</style>
</head>

<body>

<div class="container">

<h1>AWS Cloud Quiz</h1>

<div class="question">
<p><b>1. What does AWS stand for?</b></p>
<input type="radio" name="q1" value="1"> Amazon Web Services<br>
<input type="radio" name="q1" value="0"> Advanced Web System<br>
<input type="radio" name="q1" value="0"> Application Web Server
</div>

<div class="question">
<p><b>2. Which AWS service is serverless?</b></p>
<input type="radio" name="q2" value="0"> EC2<br>
<input type="radio" name="q2" value="1"> Lambda<br>
<input type="radio" name="q2" value="0"> RDS
</div>

<div class="question">
<p><b>3. Which service is used for object storage?</b></p>
<input type="radio" name="q3" value="1"> S3<br>
<input type="radio" name="q3" value="0"> Lambda<br>
<input type="radio" name="q3" value="0"> CloudWatch
</div>

<div class="question">
<p><b>4. Which database is NoSQL?</b></p>
<input type="radio" name="q4" value="1"> DynamoDB<br>
<input type="radio" name="q4" value="0"> RDS MySQL<br>
<input type="radio" name="q4" value="0"> PostgreSQL
</div>

<div class="question">
<p><b>5. Which service launches virtual servers?</b></p>
<input type="radio" name="q5" value="1"> EC2<br>
<input type="radio" name="q5" value="0"> S3<br>
<input type="radio" name="q5" value="0"> Lambda
</div>

<button onclick="checkQuiz()">Submit Quiz</button>

<div id="result"></div>

</div>

<script>
function checkQuiz(){

let score = 0;

for(let i=1;i<=5;i++){

let ans = document.querySelector('input[name="q'+i+'"]:checked');

if(ans){
score += parseInt(ans.value);
}
}

document.getElementById("result").innerHTML =
"Your Score: " + score + " / 5";
}
</script>

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