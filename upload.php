<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link href="https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&display=swap" rel="stylesheet">

    <title>Unbiased Bail</title>

    <!-- Additional CSS Files -->
    <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">

    <link rel="stylesheet" type="text/css" href="assets/css/font-awesome.css">

    <link rel="stylesheet" href="assets/css/templatemo-training-studio.css">

    </head>
    
    <body>
    
    
    <!-- ***** Header Area Start ***** -->
    <header class="header-area header-sticky">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <nav class="main-nav">
                        <!-- ***** Logo Start ***** -->
                        <a href="index.html" class="logo">Unbiased<em> Bail</em></a>
                        <!-- ***** Logo End ***** -->
                        <!-- ***** Menu Start ***** -->
                        <ul class="nav">
                            <li class="scroll-to-section"><a href="main.html" class="active">Home</a></li>
                            <li class="scroll-to-section"><a href="main.html">The Website</a></li>
                            <li class="scroll-to-section"><a href="main.html">Upload</a></li>
                            <li class="scroll-to-section"><a href="main.html">About Us</a></li>
                            <li class="scroll-to-section"><a href="main.html">Contact</a></li> 
                        </ul>        
                        <a class='menu-trigger'>
                            <span>Menu</span>
                        </a>
                        <!-- ***** Menu End ***** -->
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <!-- ***** Header Area End ***** -->
    <?php
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        if(isset($_FILES["fileToUpload"])){ 
            $filename = $_FILES["fileToUpload"]["name"];
            $filetype = $_FILES["fileToUpload"]["type"];
            $filesize = $_FILES["fileToUpload"]["size"];
            $result = "";
                if(file_exists("upload/" . $filename)){
                    $result = $filename . " is already exists. please try renaming your file";
                } else{
                    move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], "./uploads/" . $filename);
                    $result = "Your file was uploaded successfully.";
                } 
        } else{
            echo $_SERVER["REQUEST_METHOD"];
            echo "Error: " . $_FILES["photo"]["error"];
        }
    }
    $cmd = "python bail.py " .$filename;
    $output = shell_exec($cmd);

    ?>
    <!-- ***** Main Banner Area Start ***** -->
    <div class="main-banner" id="top">
        <video autoplay muted loop id="bg-video">
            <source src="assets/images/witness-stand.mp4" type="video/mp4" />
        </video>

        <div class="video-overlay header-text">
            <div class="caption">
              
                <h2>Unbiased<em>Bail</em></h2>
                <p>This person <?php $output ?> be let out on bail</p>
            
            </div>
        </div>
    </div>
    <!-- ***** Main Banner Area End ***** -->
