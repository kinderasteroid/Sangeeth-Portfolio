const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = document.querySelector("#name").value;
  const email = document.querySelector("#email").value;
  const session = document.querySelector("#session").value;

  // Validate the form

  if (name === "" || email === "" || session === "") {
    alert("Please fill in all required fields.");
    return;
  }

  // Submit the form

  const formData = new FormData(form);

  fetch("submit.php", {
    method: "GET",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Form submitted successfully.");
      } else {
        alert("There was an error submitting the form.");
      }
    })
    .catch((error) => {
      alert("There was an error submitting the form.");
    });
});