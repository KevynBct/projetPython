<!-- Home page -->
<!DOCTYPE html>
<html>
	<head>
		<title>Rechercher un sport</title>

		<!-- CSS  -->
		<style type="text/css">
			@font-face {
			    font-family: "EarthOrbiter";
			    font-style: italic;
			    src: url('/static/earthorbiter.ttf');
			}
			body 
			{
				background: url("/static/accueil.jpg") no-repeat center fixed; 
	            -webkit-background-size: cover; /* pour anciens Chrome et Safari */
	            background-size: cover; /* version standardisée */
	        }

			h1 
			{
				font-size: 500%;
	        	color: white; 
				text-align: center;
				font-family:"EarthOrbiter";
				text-shadow: 0 2px 0 #222222;
			}

			h3
			{
				
				margin-top: 15%;
				font-weight: bold ; 
				font-size: 150%;
				text-align: center;
				font-family: Helvetica;
				color :rgba(240, 240, 240, 1); 			}

			.mainDiv 
			{
				font-family: sans-serif ; 
				/*background-color: rgba(255, 255, 255, 0);*/
				width: 70%;
				height: 400px;
				margin-top: 80px;
				margin-left: 15%; 
				min-height: 20%;
				border-radius: 10px ; 
			}

			input 
			{
				position:relative;
				top: 125px;
				left: 45%;
				width: 10%;
				background: rgba(230, 230, 230, 0.9);
	            color: rgba(100, 100, 100, 1);
	            border-radius: 4px;
			}
		</style>
	</head>



	<body>
	    
		<!-- Main menu --> 
	    <div class='mainDiv'>
	    	<h1> Lebonsport </h1>
	    	<h3>Il n'y a pas besoin d'être au top pour commencer. Mais il faut commencer pour être au top.</h3>
		    <form action="" method="post">
		        <input value="Entrer" type="submit">
		    </form>
	    </div>

	</body>
</html>