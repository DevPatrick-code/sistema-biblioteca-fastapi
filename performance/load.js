import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: "10s", target: 10 },
    { duration: "10s", target: 200 },
    { duration: "30s", target: 200 },
    { duration: "10s", target: 0 },
  ],
};

const book = {
  id: 1,
  titulo: "Título do livro",
  autor: "Autor do livro",
  disponivel: true,
  ano: 1234,
}

const BACKEND_DOMAIN_NAME = __ENV.BACKEND_DOMAIN_NAME;
const BACKEND_PORT = __ENV.BACKEND_PORT;
const BACKEND_POST_ENDPOINT = `http://${BACKEND_DOMAIN_NAME}:${BACKEND_PORT}/livros`;

export default function() {
  let res = http.post(
    BACKEND_POST_ENDPOINT, 
    JSON.stringify(book), 
    {headers: {'Content-Type': 'application/json'}}
  );
  check(res, { "status is 201": (res) => res.status === 201});
  sleep(1);
}