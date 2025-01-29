const divpassword = document.getElementById("div-password");
const SrcImgs = "../imgs/password/";
const input = document.getElementById("input-password");
let akey;
let bkey;
let CtrlActive = false;

divpassword.style.height = input.offsetHeight + "px";
divpassword.style.width = input.offsetWidth + "px";
divpassword.style.left = input.offsetLeft + "px";

divpassword.addEventListener("click", () => {
  input.focus();
});

input.addEventListener("keypress", (event) => {
  if (CtrlActive === true && event.key) {
    divpassword.innerHTML = ``;
    CtrlActive = false;
  }

  if (!event.ctrlKey || event.key === "Enter") {
    let img = document.createElement("img");
    img.src = SrcImgs + Math.floor(Math.random() * 4 + 1) + ".png";
    img.style.width = "50px";
    img.style.height = "50px";
    divpassword.append(img);
  }
});

input.addEventListener("keydown", (event) => {
  if (event.key) {
    if (!akey) {
      akey = event.key;
    } else {
      if (!bkey) {
        bkey = event.key;
      } else {
        akey = bkey;
        bkey = event.key;
      }
    }
  }

  if (event.ctrlKey && (bkey === "A" || bkey === "a")) {
    CtrlActive = true;
  }

  if (event.ctrlKey && (bkey === "V" || bkey === "v")) {
    let img = document.createElement("img");
    img.src = SrcImgs + Math.floor(Math.random() * 4 + 1) + ".png";
    img.style.width = "50px";
    img.style.height = "50px";
    divpassword.append(img);
  }

  if (
    CtrlActive === true &&
    (event.key === "Backspace" || event.key === "Delete")
  ) {
    divpassword.innerHTML = ``;
    CtrlActive = false;
  }

  if (event.key === "Delete" || event.key === "Backspace") {
    divpassword.removeChild(divpassword.lastElementChild);
  }
});

