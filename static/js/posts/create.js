const form = document.getElementById("form");
const image = document.getElementById("id_image");
const caption = document.getElementById("id_caption");

image.classList.add("form-control");
caption.classList.add("form-control");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);

  const endpoint = `/api/posts/create/`;
  const method = "POST";
  const xhr = new XMLHttpRequest();
  xhr.open(method, endpoint);
  xhr.onload = () => {
    if (xhr.status === 201) {
      window.location.href = '/feed/'
    } else if (xhr.status === 401) {
      alert("Required info not given");
    } else if(xhr.status === 403){
      alert("An authentication error occurred")
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
