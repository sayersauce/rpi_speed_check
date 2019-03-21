<html>
<head>
    <title>Internet Speeds</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>xxx Internet Speed Log</h1>
    <p>This is a table of the latest internet download speed readings. Data is given in Mbps (megabits per second) ,
        for reference, 4G on mobile phones is between 4-12 Mbps.</p>
    <p>Check internet speeds on any device in the household by going to xxx.xxx.x.xx in a browser.</p>

    <h3 class="latest_speed">Latest Speed: </h3>

    <?php include_once "GetData.php"; ?>
    <br>

    <p>Program written by Max Sayer.</p>
</body>
</html>
