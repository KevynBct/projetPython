<!-- Main page and search page -->
<!DOCTYPE html>
<html>
<head>
    <title>Lebonsport</title>
    
    <!-- CSS of this page-->
    <style type="text/css">

        @font-face {
            font-family: "EarthOrbiter";
            font-style: italic;
            src: url('/static/earthorbiter.ttf');
        }

        body 
        {
            font-family : Helvetica;
            background: url("/static/curry.jpg") no-repeat center fixed; 
            -webkit-background-size: cover;
            background-size: cover;
        }

        h1 
        {
            position:relative;
            top:20px;
            left: 25%;
            width: 50%;
            text-align: center;
            font-family: "EarthOrbiter";
            font-size: 200%;
            color: rgba(230, 230, 230, 1);
            text-shadow: 0 2px 0 #222222;
        }

        table 
        {
            width : 70%;
            margin-left : 15%;
            margin-top: 15%;
            display: block;
        }

        select 
        {
            width: 90%;
            margin-left: 5%;
            height: 34px;
            overflow: hidden;
            background: url(/static/arrow.png) no-repeat right rgba(230, 230, 230, 0.9);
            color: rgba(100, 100, 100, 1);
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        td 
        {
            width: 25%;
        }

        .mainDiv
        {
            background-color: rgba(255, 255, 255, 0.2);
            width: 70%;
            height: 60%;
            margin-left: 15%;
            margin-top: 10%;
            min-height: 20%;
            border-radius: 5px;

        }
        input 
        {
            background: rgba(230, 230, 230, 0.9);
            color: rgba(100, 100, 100, 1);
            display: block;
            width: 10%;
            margin-left: 45%;
            margin-bottom: 5%;
            margin-top: 5%;
            border-radius: 4px;
        }


    </style>
</head>


<!-- Search menu -->
<body>
    <div class='mainDiv'>
        <h1> Effectuez votre recherche </h1>
        <form action="/index" method="post">
            <table>
                <tr>
                    <td>
                        <!-- Activity -->
                        <select id="activite" name="activite">
                            <option value="">Choisissez une activité</option>
                            % for nom in activite:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                    <td>
                        <!-- Location -->
                        <select id="installation" name="installation">
                            <option value="">Choisissez un lieu</option>
                            % for nom in installation:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                </tr>
            </table>
                <input value="Valider" type="submit">
            </br>
        </form>
    </div>
</body>
</html>