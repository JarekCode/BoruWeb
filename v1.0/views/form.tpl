<!DOCTYPE html>
<html>
    <!-- Font -->
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<head>
    <!-- CSS -->
    <style>
html {
    font-family: 'Roboto', sans-serif;
}
h1 {
    text-align: center;
}
p {
    text-align: center;
}
form {
    text-align: center;
}
input[type=text] {
    width: 44%;
    padding: 6px 0;
    border: 1px solid #ccc;
    font-size:16px;
}
input[type=submit] {
    width: 30%;
    background-color: #63AE45;
    padding: 10px 0;
    border: 1px solid;
    border-radius: 10px;
    color:white;
}
input[type=submit]:hover {
    background-color: #4ac44f;    
}
#theForm {
    border-radius: 15px;
    background-color: #ececec;
    padding: 20px;
}
    </style>
    
    <title>AlienVault - Start Lab</title>
</head>
<body>
    <h1>Start Lab</h1>
    <!-- The Form -->
    <div id="theForm">
    <form action="/boru/form" method="post">
        <!-- Pattern: Only Allow a-z A-Z 0-9, no special characters -->
	<!-- Only One User, no special characters prevent from entering more than one. Only one user to prevent .log file from breaking the naming convention in bottle -->
	Account Name:<br>
        <input type="text" name="field1" autocomplete="off" pattern="[a-zA-Z0-9]*" placeholder=" Example:  AVStudentXXX" required>
        <br><br>
	<!-- Pattern: Special characters allowed except " or ' to prevent the labStart script from breaking -->
        Password:<br>
        <input type="text" name="field2" autocomplete="off" pattern="[\w!€£$%^&*()_+{}\[\]:;@#~?.>,<`¬\-=]*" required>
        <br><br>
	<!-- Server Region -->
        Region:<br>
        <select name="field3" style="width:44%; height:30px;">
            <option value="us-east-1">US East 1</option>
        </select>
        <br><br>
	<!-- Name of the Course -->
        Course:<br>
        <select name="field4" style="width:44%; height:30px;">
            <option value="ANYDC">ANYDC</option>
        </select>
        <br><br>
	<!-- Set up Sensor -->
        Sensor:<br>
        <select name="field5" style="width:44%; height:30px;">
            <option value="yes">Yes</option>
            <option value="no">No</option>
        </select>
        <br><br>
	<!-- Identification Tag -->
        <!-- No special characters allowed except -  -->
	Tag:<br>
        <input type="text" name="field6" autocomplete="off" pattern="[a-zA-Z0-9\-]*[a-zA-Z0-9]" placeholder=" Example:  EU-May16-17-OC" required>
	<br><br>
	<!-- labFinish Script Date -->
        End Date:<br>
        <input type="date" name="field8" style="width:44%; height:30px;" required>
        <br><br>
	<!-- Timezone  -->
        Timezone:<br>
        <select name="field9" style="width:44%; height:30px;">
            <option value="WET">WET (Cork)</option>
            <option value="CET">CET (Paris)</option>
            <option value="EST">EST (New York)</option>
            <option value="CST">CST (Austin)</option>
            <option value="PST">PST (San Francisco)</option>
            <option value="APJ">APJ (Sydney)</option>
        </select>
        <br><br>
	<!-- Submit Button  -->
        <input type="submit" value="Start Lab">
    </form> 
    </div><br><br><br>
</body>
</html>
%rebase base
