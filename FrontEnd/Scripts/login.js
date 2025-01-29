const url = "https://classmood-wdmz.onrender.com";
const form = document.querySelector("form");
const alertError = document.getElementById("error");

form.addEventListener("submit", (event) => {
  alertError.style.display = "none";
  event.preventDefault();

  const formData = new FormData(form);
  const loginData = Object.fromEntries(formData);

  fetch(url + "/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginData),
  })
    .then((res) => {
      console.log(res.status);
      switch (res.status) {
        case 201:
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
