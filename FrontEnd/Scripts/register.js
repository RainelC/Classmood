const form = document.querySelector("form");
const inputt = document.getElementById("input-password");

inputt.addEventListener("keydown", () => {

  const formData = new FormData(form);
  const loginData = Object.fromEntries(formData);
    console.log(loginData)


  let name = loginData.name;
  let lastname = loginData.lastname;
//   let email = loginData.email;
  let password = loginData.password;

  if(name.length > 0 && lastname.length > 0 && password.length > 6)
  {
    scroll(0,90);
  }

})

