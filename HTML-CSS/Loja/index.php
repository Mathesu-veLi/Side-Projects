<?php

include 'config.php';
session_start();

function send_whatsapp($message = "Test")
{
    $phone = "+557197044006";  // Enter your phone number here
    $apikey = "2078976";       // Enter your personal apikey received in step 3 above

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
$user_id = $_SESSION['user_id'];
$user_name = $_SESSION['user_name'];
if (isset($_GET['pay'])) {
    if (!isset($user_id)) {
        header('location:login.php');
    } else {
        $cart_query = mysqli_query($conn, "SELECT * FROM `cart` WHERE user_id = '$user_id'") or die('query failed');
        $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE id = '$user_id'") or die('query failed');
        $row = mysqli_fetch_assoc($select);
        $items = '';
        $grand_total = 0;
        if (mysqli_num_rows($cart_query) > 0) {
            while ($fetch_cart = mysqli_fetch_assoc($cart_query)) {
                $items .= "{$fetch_cart['name']} ({$fetch_cart['quantity']})  ";
                $grand_total += $fetch_cart['price'] * $fetch_cart['quantity'];
                mysqli_query($conn, "DELETE FROM `cart` WHERE id = {$fetch_cart['id']}") or die('query failed');
            }
            mysqli_query($conn, "INSERT INTO `orders` (user_id, user_name, items) VALUES ('$user_id', '$user_name', '$items')") or die('query failed');
            $grand_total = 'R$' . number_format($grand_total, 2);
            send_whatsapp("Nova compra na OUV-Shop!\nO usuário {$user_name} acaba de comprar {$items}\nO preço total foi de {$grand_total}\nO endereço de {$user_name} é:\nCEP: {$row['cep']}\nEstado: {$row['estado']}\nCidade: {$row['cidade']}\nRua: {$row['rua']}\nNúmero: {$row['numero']}\nComplemento: {$row['complemento']}");
        }
    }
}

if (isset($_GET['logout'])) {
    unset($user_id);
    session_destroy();
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
    <script src="https://kit.fontawesome.com/0a970faf9c.js" crossorigin="anonymous"></script>
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
            <ul class="nav-menu" style="width: 100%; justify-content: center;">
                <li class="nav-item"><a href="index.php" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="comprar.php" class="nav-link">Comprar</a></li>
                <li class="nav-item"><a href="contato.php" class="nav-link">Contato</a></li>
                <?php if (isset($user_id)) {

                    $user_name = $_SESSION['user_name'];
                    echo '
                            <li class="dropdown">
                                <p style="color: white">' . $user_name . '&nbsp&nbsp<i class="fas fa-chevron-down"></i></p>
                                <ul>
                                    <li><a href="index.php?logout">Logout</a></li>
                                </ul>
                            </li>
                            ';
                } ?>
            </ul>
            <a href="cart.php"><img src="img/shopping-cart-white.png" alt="Carrinho" width="50"></a>
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