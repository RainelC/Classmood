// const url = "https://classmood-wdmz.onrender.com";
const url = "http://127.0.0.1:8000";
const form = document.querySelector("form");
const alertError = document.getElementById("error");

form.addEventListener("submit", (event) => {
  alertError.style.display = "none";
  event.preventDefault();

  const formData = new FormData(form);
  const loginData = Object.fromEntries(formData);

  fetch(url + "/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams(loginData).toString(),
  })
    .then((res) => {
      console.log(res.status);
      switch (res.status) {
        case 200:
          return res.json();
        case 400:
          alertError.firstElementChild.innerHTML = `Invalid email or password.`;
          alertError.style.display = "block";
          break;
        case 401:
          alertError.firstElementChild.innerHTML = `Invalid password`;
          alertError.style.display = "block";
          break;
        default:
        //   console.log("default");
        // Hacer retonar a una página que diga "Internal error" + code error
          break;
      }
    })
    .then((data) => {
      if (data){
        window.open("../HTML/index.html", "_parent");
      }
    })
    .catch(console.error());
});
