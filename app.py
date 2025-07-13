from flask import Flask
app = Flask (__name__)
@app.route("/")
def flaskinfo():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Capture Photo</title>
  <style>
    video, canvas {
      display: block;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <video id="video" width="320" height="240" autoplay></video>
  <button onclick="takePhoto()">Capture Photo</button>
  <canvas id="canvas" width="320" height="240"></canvas>

  <script>
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');

    // Access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        video.srcObject = stream;
      })
      .catch(error => {
        console.error("Webcam access error:", error);
        alert("Please allow access to the camera.");
      });

    // Capture the photo
    function takePhoto() {
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      // Optional: Save the image
      canvas.toBlob(blob => {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'photo.png';
        link.click();
      });
    }
  </script>
</body>
</html> """
if __name__=="__main__":
    app.run(host="0.0.0.0" , port="5000")