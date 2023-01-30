<?php

include 'config.php';
session_start();

function send_whatsapp($message = "Test")
{
    $phone = "+557185076263";  // Enter your phone number here
    $apikey = "6017675";       // Enter your personal apikey received in step 3 above

    $url = 'https://api.callmebot.com/whatsapp.php?source=php&phone=' . $phone . '&text=' . urlencode($message) . '&apikey=' . $apikey;

    if ($ch = curl_init($url)) {
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        $html = curl_exec($ch);
        $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        // echo "Output:".$html;  // you can print the output for troubleshooting
        curl_close($ch);
        return (int) $status;
    } else {
        return false;
    }
}

if (isset($_GET['pay'])) {
    $user_id = $_SESSION['user_id'];
    $user_name = $_SESSION['user_name'];
    if (!isset($user_id)) {
        header('location:login.php');
    } else {
        $cart_query = mysqli_query($conn, "SELECT * FROM `cart` WHERE user_id = '$user_id'") or die('query failed');
        $items = '';
        if (mysqli_num_rows($cart_query) > 0) {
            while ($fetch_cart = mysqli_fetch_assoc($cart_query)) {
                $items .= "{$fetch_cart['name']} ({$fetch_cart['quantity']})  ";
                mysqli_query($conn, "DELETE FROM `cart` WHERE id = {$fetch_cart['id']}") or die('query failed');
            }
            mysqli_query($conn, "INSERT INTO `orders` (user_id, user_name, items) VALUES ('$user_id', '$user_name', '$items')") or die('query failed');
            send_whatsapp("Nova compra na OUV-Shop!\nO usuário {$user_name} acaba de comprar {$items}");
        }
    }
}

?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
    <title>OUV Trajes</title>
</head>

<body>
    <header>
        <nav class="navbar">
            <div class="hamb">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
            <a href="" class="logo"><img src="img/logo.png" alt="logo" width="180"></a>
            <ul class="nav-menu">
                <li class="nav-item"><a href="index.php" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="comprar.html" class="nav-link">Comprar</a></li>
                <li class="nav-item"><a href="contato.html" class="nav-link">Contato</a></li>
            </ul>
            <div style="display: flex;flex-direction: row;">
                <a href="cart.php"><img src="img/shopping-cart-white.png" alt="Carrinho" width="50"></a>
            </div>
        </nav>
    </header>

    <main>
        <div class="promo">
            <div class="escurecer">
                <h1>Promoção!</h1>
            </div>
        </div>
        <div class="about"></div>

        <div class="sobre">
            <center class="title">
                <h2>Sobre</h2>
            </center>
            <div class="imgs">
                <div class="img"><img src="https://static1.s123-cdn-static-a.com/uploads/7229753/400_639c11907008b.jpg" alt="Camisa 2"></div>
                <div class="img"><img src="https://static1.s123-cdn-static-a.com/uploads/7229753/400_639c0ff9d0970.jpg" alt="Camisa 1"></div>
                <div class="img"><img src="https://static1.s123-cdn-static-a.com/uploads/7229753/400_639c10fbe322c.jpg" alt="Camisa 3"></div>
            </div>
            <div class="conteiner">
                <p>Especializada em camisas de futebol e artigos esportivos, a loja virtual surgiu em 2022 na cidade de Salvador (BA) e reúne uniformes completos dos mais variados clubes brasileiros, internacionais e seleções - dos mais consagrados aos menos conhecidos. Com a maior variedade em camisas de times de futebol no mercado nacional, a OUV trabalha em parceria com as principais marcas esportivas para comercializar somente produtos originais e com garantia de qualidade. Além disso, a loja possui certificados de segurança que oferecem ao cliente um ambiente de compra confiável.</p>
            </div>
        </div>

        <div class="nw-clct">
            <center class="title">
                <h2>Nova Coleção</h2>
            </center>
            <div class="new-center">
                <div class="camisa">
                    <a href="produtos/Camisa-da-Argentina.php">
                        <div class="arg">
                            <div class="arg-camisa">
                                <img src="https://static1.s123-cdn-static-a.com/uploads/7229753/400_639c10fbe322c.jpg" alt="Camisa da Argentina">
                            </div>
                            <div class="new-title">
                                <h1>Camisa da Argentina</h1>
                                <div class="precos">
                                    <h2><small><del>R$399</del></small></h2>
                                    <h2>R$146</h2>
                                </div>
                            </div>
                            <br>
                            <p>• Camisa 100% poliéster; • Logotipo da marca bordado; • Logotipo da equipe bordado; • Tecnologia anti-...</p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </main>
    <script src="mobile-menu.js"></script>
</body>

</html>