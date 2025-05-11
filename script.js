document
  .getElementById("locationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let location = document.getElementById("location").value;
    getResult(location);
  });

function getResult(location) {
  // Simulating an API call (Replace with actual API URL)
  fetch(`https://api.example.com/location?name=${location}`)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "locationDetails"
      ).innerHTML = `<p>${data.details}</p>`;
    })
    .catch((error) => {
      document.getElementById(
        "locationDetails"
      ).innerHTML = `<p>Error fetching details. Try again!</p>`;
      console.error("Error:", error);
    });
}
