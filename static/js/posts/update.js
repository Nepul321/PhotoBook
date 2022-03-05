const form = document.getElementById("form");
const container = document.getElementById("container");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  const id = container.dataset.id;
  const endpoint = `/api/posts/${id}/update/`;
  const method = "POST";
  const xhr = new XMLHttpRequest();
  xhr.open(method, endpoint);
  xhr.onload = () => {
    if (xhr.status === 200) {
      window.location.href = `/posts/${id}/`;
    } else if (xhr.status === 401) {
        alert("Required info not given");
    } else if (xhr.status === 403) {
      const response = JSON.parse(xhr.response);
      const message = response.detail;
      if (message) {
        alert(message);
      }
      alert("An authentication error occurred.")
    } else if (xhr.status === 500) {
      alert("Please try again");
    }

    form.reset();
  };

  xhr.onerror = () => {
    alert("An error occurred. Please try again");
  };

  xhr.send(formData);
});
