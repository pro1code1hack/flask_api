let blog = document.querySelector(".blog-container");
let data = [];
async function renderData() {

    let response = await fetch('http://127.0.0.1:5000/posts');

    if (response.ok) {
        data = await response.json();
    } else {
        alert('error', response.status);
    }
    
    data.forEach(item => {
        blog.innerHTML += 
        `
        <div class="blog-box">
        <div class="blog-img">
            <img src="${item.rendered_data_of_pic}" alt="post">
        </div>
        <div class="blog-text">
            <span>${item.posted_date}</span>
            <a href="" class="blog-title"> ${item.title} </a>
            <p>${item.description}</p>
            <p>${item.url}</p>

            <a href="#">Read More</a>
        </div>
    </div>
        `;
    })
}

renderData();