<!DOCTYPE html>
<html lang="en">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="icon" href="/static/images/smallLogo.jpg">
<head>
    <!-- CSS -->
    <style>
html {
    text-align: center;
    font-family: 'Roboto', sans-serif;
}
body {
    margin-left: 20%;
    margin-right: 20%;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #63AE45;
    color: white;
    text-align: center;
}
ul {
  list-style-type: none;
  position: fixed;
  top: -16px;
  left: 0;
  width: 100%;

  overflow: hidden;
  background-color: #323B43;
}
li {
  float: left;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover:not(.active) {
  background-color: #63AE45;
}
    </style>

    <title>AlienVault</title>
</head>
<body>
    <!-- Navigation Menu -->
    <ul>
        <li><a href="/boru/home">Home</a></li>
        <li><a href="/boru/form">Start Lab</a></li>
    </ul>
    <br><br><br><br>
    <!-- Logo -->
    <img src="/static/images/logo.png" alt="AlienVault Logo" height="100">
    <!-- %include -->
    <div id="pagebody">
        %include
    </div>
    <!-- Footer -->
    <div class="footer">
        <p>AlienVault</p>
    </div>
</body>
</html>
