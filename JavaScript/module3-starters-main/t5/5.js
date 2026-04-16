'use strict';

const section = document.getElementById('pictures');

for (const pic of picArray) {
  // <article class="card">
  const article = document.createElement('article');
  article.classList.add('card');

  // <h2>title</h2>
  const h2 = document.createElement('h2');
  h2.textContent = pic.title;

  // <figure>
  const figure = document.createElement('figure');

  // <img src="..." alt="...">
  const img = document.createElement('img');
  img.src = pic.image.medium;
  img.alt = pic.title;

  // <figcaption>caption</figcaption>
  const figcaption = document.createElement('figcaption');
  figcaption.textContent = pic.caption;

  // Add img + caption to figure
  figure.appendChild(img);
  figure.appendChild(figcaption);

  // <p>description</p>
  const p = document.createElement('p');
  p.textContent = pic.description;

  // Build article
  article.appendChild(h2);
  article.appendChild(figure);
  article.appendChild(p);

  // Add article to <section>
  section.appendChild(article);
}
