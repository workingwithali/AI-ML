function toggleMatrixB(operation) {
  const container = document.getElementById("matrixB-container");
  if (operation === "transpose" || operation === "inverse") {
    container.style.display = "none";
  } else {
    container.style.display = "block";
  }
}

window.onload = () => {
  const select = document.querySelector("select");
  toggleMatrixB(select.value);
  select.addEventListener("change", (e) => toggleMatrixB(e.target.value));
};
