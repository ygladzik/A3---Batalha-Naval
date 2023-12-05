const endpoint = "http://localhost:8000/top3";

fetch(endpoint, {
    method: 'GET',
    mode: 'cors',
})
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.statusText}`);
    }
    return response.json();
  })
  .then((data) => {
    const rankBody = document.getElementById("rank");

  
    data.forEach((player, index) => {
      const row = document.createElement("tr");

      
      const rankCell = document.createElement("td");
      rankCell.textContent = index + 1;
      rankCell.classList.add("celula_rank")
      row.appendChild(rankCell);

      const jogadorCell = document.createElement("td");
      jogadorCell.textContent = player.apelido; 
      row.appendChild(jogadorCell);

      const pontuacaoCell = document.createElement("td");
      pontuacaoCell.textContent = player.pontuacao; 
      row.appendChild(pontuacaoCell);

    
      rankBody.appendChild(row);
    });
  })
  .catch((err) => console.error("Erro:", err));