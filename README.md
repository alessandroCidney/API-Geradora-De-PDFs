# API Geradora de PDFs :snake:

## Como utilizar

### Acionando a API
- No diretório do projeto, por meio do Prompt de Comando, utilize o comando `py app.py`
- A API será ativada e poderá ser utilizada através de `http://localhost:5000`

### Usando a API
- Para criar um PDF, basta realizar uma requisição de método POST para a rota `/test`, passando no corpo da requisição do nome do arquivo (sem extensão) por meio de "filename" e o conteúdo por meio de "content"

Exemplo com JavaScript:
```javascript
let results = await fetch('http://localhost:5000/test', {
	method: 'POST',
	headers: {
		"Content-Type": "application/json"
	},
	body: JSON.stringify({
		filename: "filename",
		content: "content"
	})
})
.then(response => response.json())
.then(data => data)
.catch(err => err);
```

### Retorno
- A API retorna um JSON contendo o local do arquivo (que será gerada na mesma pasta de app.py), o formato do arquivo (PDF) e se houve algum erro

Exemplo:
```json
{
	"local_do_arquivo": "...",
	"formato": "PDF",
	"houveram_erros": "Sim/Não"
}
```

