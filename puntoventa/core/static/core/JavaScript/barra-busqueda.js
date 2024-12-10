document.addEventListener('DOMContentLoaded', function () {
    const inputBuscador = document.querySelector('[name="busqueda_producto"]');
    const resultadosDiv = document.getElementById('resultados_busqueda');

    async function obtenerSugerencias(query) {
        if (query.length < 2) {
            resultadosDiv.innerHTML = '';
            return;
        }

        try {
            const response = await fetch('/buscar-productos/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ query })
            });

            const data = await response.json();

            if (data.success) {
                mostrarSugerencias(data.resultados);
            }
        } catch (error) {
            console.error('Error al buscar sugerencias', error);
        }
    }

    function mostrarSugerencias(sugerencias) {
        resultadosDiv.innerHTML = '';
        sugerencias.forEach(producto => {
            const div = document.createElement('div');
            div.textContent = producto.nombre;
            div.classList.add('sugerencia');
            div.onclick = function () {
                inputBuscador.value = producto.nombre;
                resultadosDiv.innerHTML = '';
            };
            resultadosDiv.appendChild(div);
        });
    }

    inputBuscador.addEventListener('input', function (e) {
        obtenerSugerencias(e.target.value);
    });

    function getCSRFToken() {
        let cookieValue = null;
        const name = 'csrftoken';
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});