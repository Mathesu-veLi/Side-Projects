<?php

    include 'config.php';
    if(isset($_POST['submit']))
    {
        $name = mysqli_real_escape_string($conn, $_POST['name']);
        $email = mysqli_real_escape_string($conn, $_POST['email']);
        $pass = mysqli_real_escape_string($conn, $_POST['password']);
        $cpass = mysqli_real_escape_string($conn, $_POST['cpassword']);

        $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE email = '$email' AND password = '$pass'") or die('query failed');

        if(mysqli_num_rows($select) > 0)
        {
            $message[] = 'Usuario ja cadastrado!';
        }else{
            mysqli_query($conn, "INSERT INTO `user_form`(name, email, password) VALUES('$name', '$email', '$pass')") or die('query failed');
            $message[] = 'Usuario registrado com sucesso!';
        }
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro - OUV Trajes</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/font.css">
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
</head>
<body class="regs-log">


    <?php

        if(isset($message))
        {
            foreach($message as $message)
            {
                echo '<div class="message" onclicl="this.remove();">'.$message.'</div>';
            }
        }

    ?>


    <div class="form-container">
        <form action="" method="post">
            <h3>Cadastro</h3>
            <input type="text" name="name" placeholder="Nome" required class="box">
            <input type="email" name="email" placeholder="Email" required class="box">
            <input type="password" name="password" placeholder="Senha" required class="box">
            <input type="password" name="cpassword" placeholder="Confirme sua senha" required class="box">
            <input type="submit" name="submit" class="btn" value="Registre-se">
            <p>Já tem uma conta? Faça<a href="login.php">login</a></p>
        </form>
    </div>
</body>
</html>