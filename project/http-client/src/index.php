<html>

<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        body {
            font-family: 'Raleway', sans-serif;
            color: black;
            background: no-repeat;
            background-size: 100%;
            background-image: url('https://luxoboi.com.ua/pic/product_foto/prodfoto7036.jpg'); 
            /* поменять бэк */
        }
        .button {
            background-color: #8A2BE2; 
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-weight: bold;
            font-size: 20px;
            border-radius: 12px;
        }
        .content{
            font-weight: bold;
            font-size: 20px;
        }
        .th-style{
            font-weight: bold;
            font-size: 20px;
        }    

    </style>
</head>

<body>
    <div class="container form">
        <div class="container-fluid">
            <h2>Заказы</h2>
        </div>


        <form action="index.php" method="post">
            <input type="hidden" name="output" id="output" value=1>
            <button type="submit" class="button">До удаления</button>
        </form>
        <form action="index.php" method="post">
            <input type="hidden" name="del" id="del" value=1>
            <button type="submit" class="button">После удаления</button>
        </form>
    </div>
    <br><br>
    <table class="table table-condensed">
       
            <?php
            if (isset($_POST['del'])) {
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/test/',
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                echo '<thead class="thead-dark">
                <th class="th-style">Excelid</th>
                <th class="th-style">Myid</th>
                <th class="th-style">id Order</th>
                <th class="th-style">Client Name</th>
                <th class="th-style">Client Surname</th>
                <th class="th-style">Order date</th>
                <th class="th-style">Price</th>
                </thead>
                <tbody>';
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                $json = json_decode($response, true);
                $zadacha = $json['zadacha'];
                for ($i = 0; $i <= count($zadacha['price']); $i++) {
                    // $zadacha as $value
                    echo "<tr>";
                    foreach ($zadacha as $key => $value) {
                        
                        echo "<td class='content'>" .  $value[$i] . "</td>";
                    }
                    echo "</tr>";
                }
            }
            if (isset($_POST['output'])) {

                    $myCurl = curl_init();
                    curl_setopt_array(
                        $myCurl,
                        array(
                            CURLOPT_URL => 'http://nginxserver/main/',
                            CURLOPT_RETURNTRANSFER => true,
                            CURLOPT_HEADER => false,

                        )
                    );
                    $response = curl_exec($myCurl);
            
                    curl_close($myCurl);
                    echo $response;
                }
            ?>
        </tbody>
    </table>
 </body>

</html>