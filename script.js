document
  .getElementById("locationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let location = document.getElementById("location").value;
    getResult(location);
  });

function getResult(location) {
  // Simulating an API call (Replace with actual API URL)
  fetch(
    `https://3n01r6q2rj.execute-api.us-east-1.amazonaws.com/dev?locationId=${location}`
  )
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "locationDetails"
      ).innerHTML = `<p>${data.gpt_response}</p>`;
    })
    .catch((error) => {
      document.getElementById(
        "locationDetails"
      ).innerHTML += `<p>Error fetching details. Try again!</p>`;
      console.error("Error:", error);
    });
}
