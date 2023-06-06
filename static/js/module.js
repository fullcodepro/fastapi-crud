const btnEnviar = document.querySelector('#btn-enviar');
const historyList = document.querySelector('#history-list');

// const mostrarRespuesta = (respuesta) => {
//     const li = document.createElement('li');
//     li.classList.add('list-item', 'd-flex', 'justify-content-center', 'align-items-center', 'text-center', 'px-3', 'respuesta');
//     const p = document.createElement('p');
//     p.innerText = respuesta;
//     li.appendChild(p);
//     historyList.appendChild(li);
//     scrollToBottom(historyList);
// }

const mostrarRespuesta = (respuesta) => {
    const li = document.createElement('li');
    li.classList.add('list-item', 'd-flex', 'align-items-center', 'px-3', 'respuesta');
  
    const respuestaContainer = document.createElement('span');
    respuestaContainer.classList.add('respuesta-container', 'respuesta');
    li.appendChild(respuestaContainer);
  
    historyList.appendChild(li);
    scrollToBottom(historyList);
  
    let index = 0;
  const mostrarSiguienteLetra = () => {
    if (index < respuesta.length) {
      const textoParcial = respuesta.substring(0, index + 1);
      respuestaContainer.textContent = textoParcial;
      index++;
      // Ajusta el tiempo entre cada letra (en milisegundos) para controlar la velocidad de la respuesta
      const tiempoEntreLetras = 14; // Puedes ajustar este valor según tus necesidades
      setTimeout(mostrarSiguienteLetra, tiempoEntreLetras);
    }
  };
  
    mostrarSiguienteLetra();
  };
  

const mostrarPregunta = (pregunta) => {
    const li = document.createElement('li');
    li.classList.add('list-item', 'd-flex', 'justify-content-center', 'align-items-center', 'text-center', 'px-3', 'pregunta');
    const p = document.createElement('p');
    p.innerText = pregunta;
    li.appendChild(p);
    historyList.appendChild(li);
    scrollToBottom(historyList);
}

// Función para hacer scroll hasta el fondo de un elemento
const scrollToBottom = (element) => {
    element.scrollTop = element.scrollHeight - element.clientHeight;
}

btnEnviar.addEventListener('click', async (e) => {
    e.preventDefault();

    const question = document.querySelector('#input-question');

    // Se realiza una copia profunda de la pregunta
    const pregunta = question.value;
    question.value = '';

    mostrarPregunta(pregunta);
    const response = await fetch(`http://localhost:8000/falcon?question=${pregunta}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    mostrarRespuesta(data);
});
