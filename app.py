from flask import Flask
app = Flask (__name__)
@app.route("/")
def flaskinfo():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Color Changer</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      transition: background-color 0.5s ease;
    }

    .container {
      text-align: center;
    }

    h1 {
      margin-bottom: 20px;
    }

    button {
      padding: 12px 24px;
      font-size: 18px;
      border: none;
      border-radius: 8px;
      background-color: #333;
      color: #fff;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #555;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Click to Change Background Color</h1>
    <button onclick="changeColor()">Change Color</button>
  </div>

  <script>
    const colors = ["#FF6B6B", "#6BCB77", "#4D96FF", "#FFC75F", "#B980F0"];

    function changeColor() {
      const randomColor = colors[Math.floor(Math.random() * colors.length)];
      document.body.style.backgroundColor = randomColor;
    }
  </script>
</body>
</html>
 """
if __name__=="__main__":
    app.run(host="0.0.0.0" , port="5000")