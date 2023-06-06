const btnEnviar = document.querySelector('#btn-enviar');
const historyList = document.querySelector('#history-list');

const mostrarRespuesta = (respuesta) => {
    const li = document.createElement('li');
    li.classList.add('list-group-item', 'mb-1', 'text-center', 'respuesta');
    li.innerHTML = respuesta;
    historyList.append(li);
}

const mostrarPregunta = (pregunta) => {
    const li = document.createElement('li');
    li.classList.add('list-group-item', 'mb-1', 'text-center', 'text-black', 'pregunta');
    li.innerHTML = pregunta;
    historyList.append(li);
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
    console.log(data)
    mostrarRespuesta(data);
});