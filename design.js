function makeGrid(x, y) {
  const canvas = document.getElementById("pixelCanvas");
  let grid = "";
  for (let i = 0; i < x; i++) {
    grid += "<tr>";
    for (let j = 0; j < y; j++) {
      grid +=
        '<td class="cell" id="row-' +
        i +
        "_cell-" +
        j +
        '">click for color</td>';
    }
    grid += "</tr>";
  }
  pixelCanvas.innerHTML = grid;
  colorCells();
}

function getSize() {
  const x = document.getElementById("inputHeight").value;
  const y = document.getElementById("inputWidth").value;
  makeGrid(x, y);
}

function colorCells() {
  const colorPicker = document.getElementById("colorPicker");
  const cells = document.getElementsByClassName("cell");
  for (let i = 0; i < cells.length; i++) {
    cells[i].addEventListener("click", function (event) {
      let clickCell = event.target;
      clickCell.style.backgroundColor = colorPicker.value;
    });
  }
}

document.getElementById("sizePicker").addEventListener("submit", function (event) {
  event.preventDefault();
  getSize();
});


makeGrid(5, 5);
