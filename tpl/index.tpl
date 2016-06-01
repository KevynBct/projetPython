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
            background-repeat:no-repeat;
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
            font-size: 250%;
            color: rgba(230, 230, 230, 1);
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
            height: 400px;
            margin-left: 15%;
            margin-top: 80px;
            min-height: 20%;
            border-radius: 5px;
            box-shadow: 2px 2px 0 0 grey;

        }
        input 
        {
            background: rgba(230, 230, 230, 0.9);
            color: rgba(100, 100, 100, 1);
            display: block;
            width: 10%;
            margin-left: 45%;
            margin-top: 10%;
            border-radius: 4px;
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
            <input value="Valider" type="submit">
        </form>
    </div>
</body>
</html>