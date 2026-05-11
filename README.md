# Apuntes-An-lisis-y-desarrollo-de-software

<h1>Edite una parte  </h1>
<P> EJEMPLO:
<!DOCTYPE html>
<html>
<body>
    <form action="/login.php" id="formulario">
        <p>
            Usuario: <input type="text" name="usuario" id="usuario">
        </p>
        <p>
            Clave: <input type="password" name="clave" id="clave">
        </p>
        <input type="submit" value="Entrar">
    </form>
    <script>    
        document.addEventListener('DOMContentLoaded', function () {
            document.getElementById('formulario').addEventListener('submit', validarFormulario); 
        });
        function validarFormulario(evento) {
            evento.preventDefault();
            var usuario = document.getElementById('usuario').value;
            if(usuario.length == 0) {
                alert('Por favor, ingresa un nombre de usuario.');
                return;
            }
            var clave = document.getElementById('clave').value;
            if(clave.length < 6) {
                alert('La clave debe tener al menos 6 caracteres.');
                return;
            }
            this.submit();
        }
    </script>
</body>
</html>

</P>


<H2>   EJEMPLO #2<H/2>
<p><!DOCTYPE html>
<html>
<body>
    <button id="miBoton" onclick="alert('¡Haz hecho clic en el botón!')">Haz clic</button>
    <script>
        document.getElementById('miBoton').addEventListener('click', function () {
            alert('¡Haz hecho clic aquíí con el document!');
        });
    </script>
</body>
</html>

<h3> ejemplo 3 </h3>
<!DOCTYPE html>
<html>
  <body>
    <h1 id="title">Hola Mundo</h1>
    <button onclick="cambiarTexto()">Cambiar texto</button>
    <script>
      function cambiarTexto() {
        document.getElementById('title').innerHTML = 'Texto Cambiado!';
      }
    </script>
  </body>
</html>

<h1> * Media Query para pantallas más pequeñas (máximo 600px de ancho) */
@media (max-width: 600px) {

    /* Ajustar el tamaño del encabezado */
    header h1 {
        font-size: 24px;
        color: black;
    }

    /* Sección de contenido en una sola columna */
    .main-content {
        flex-direction: column;
        align-items: center;
    }

    .main-content .section {
        width: 80%;
        /* Las secciones ocupan el 80% del ancho */
        margin-bottom: 20px;
    }

    /* Pie de página se adapta */
    footer {
        padding: 15px 0;
    }
}

/*aqui se aplica los estilos cuando el  
ancho de la pantalla es mayor o igual al valor especificado.*/
@media (min-width: 1024px) {
    header h1 {
        color: #f4d03f;
        text-decoration: underline white;
        /* Subrayado white */
    }
}

/* pantalla está en modo retrato, la altura de la pantalla es mayor que su anchura.
Por ejemplo, un celular en posición vertical.*/
@media (orientation: portrait) {
    header h1 {
        font-size: 24px;
        color: #5dade2;
        text-decoration: underline white;
    }
}

/* Estilo para orientación horizontal (paisaje) */
@media (orientation: landscape) {
    body {
        background-color: lightgreen;
    }
}

@media (min-resolution: 192dpi) {

    /* Estilo para pantallas de alta resolución (192 dpi o más) */
    body {
        background-color: lightblue;
        /* Fondo azul claro en pantallas de alta resolución */
    }

    img {
        /* Cargar imágenes de mayor calidad en pantallas de alta resolución */
        content: url('imagenx.jpg');
    }
}



////////////////////////////////////////////////////////////////////////////////////////////////
´TIPOS DE INPUTS´
<div class="mb-3">
        <label for="formFile" class="form-label">Ejemplo de entrada de archivo predeterminado</label>
        <input class="form-control" type="file" id="formFile">
    </div>
    <div class="mb-3">
        <label for="formFileMultiple" class="form-label">Ejemplo de entrada de varios archivos</label>
        <input class="form-control" type="file" id="formFileMultiple" multiple>
    </div>
    <div class="mb-3">
        <label for="formFileDisabled" class="form-label">Ejemplo de entrada de archivo deshabilitada</label>
        <input class="form-control" type="file" id="formFileDisabled" disabled>
    </div>
    <div class="mb-3">
        <label for="formFileSm" class="form-label">Ejemplo de entrada de archivo pequeño</label>
        <input class="form-control form-control-sm" id="formFileSm" type="file">
    </div>
    <div>
        <label for="formFileLg" class="form-label">Ejemplo de entrada de archivo grande</label>
        <input class="form-control form-control-lg" id="formFileLg" type="file">
    </div>
