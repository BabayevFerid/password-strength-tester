async function checkPassword() {
  const password = document.getElementById("password").value;
  const res = await fetch("http://127.0.0.1:5000/api/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password })
  });
  const data = await res.json();

  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = `
    Strength: <span class="${data.strength.toLowerCase()}">${data.strength}</span><br>
    Score: ${data.score}/5
  `;
}
