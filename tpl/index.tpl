<!-- Page de recherche et page principale du site -->
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <!-- CSS de cette page -->
    <style type="text/css">
        body 
        {
            font-family : Helvetica;
            background: url("/static/curry.jpg"); 
            background-size: 100%;
        }

        h1 
        {
            position:relative;
            top:20px;
            left: 25%;
            width: 50%;
            text-align: center;
            font-family: Impact;
        }

        table 
        {
            width : 70%;
            margin-left : 15%;
        }

        select 
        {
            position:relative;
            top: 100px;
            width : 100%;
        }

        td 
        {
            width: 25%;
        }

        .mainDiv
        {
            background-color: rgba(255, 255, 255, 0.2);
            width: 70%;
            height: 400px;
            margin-left: 15%;
            margin-top: 80px;
            min-height: 20%;
            border-radius: 5px;
            box-shadow: 2px 2px 0 0 grey;

        }

        input 
        {
            position:relative;
            top: 260px;
            left: 45%;
            width: 10%;
        }
    </style>
</head>
<body>
    <div class='mainDiv'>
        <h1> Effectuez votre recherche </h1>
        <form action="/index" method="post">
            <table>
                <tr>
                    <td>
                        <select id="activite" name="activite">
                            <option value="">Choisissez une activité</option>
                            % for nom in activite:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                    <td>
                        <select id="installation" name="installation">
                            <option value="">Choisissez un lieu</option>
                            % for nom in installation:
                                <option value="{{nom[0]}}">{{nom[0]}}
                            %end 
                        </select>
                    </td>
                </tr>
            </table>
            </br>
            <input value="Valider" type="submit">
        </form>
    </div>
</body>
</html>