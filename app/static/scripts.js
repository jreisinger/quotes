//https://github.com/taniarascia/sandbox/tree/master/ghibli

const app = document.getElementById('root');

const logo = document.createElement('img');
logo.src = 'logo.png';

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(logo);
app.appendChild(container);

var request = new XMLHttpRequest();
//request.open('GET', 'https://ghibliapi.herokuapp.com/films', true);
request.open('GET', 'http://localhost:5000/api/v1/all/', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  //console.log(JSON.stringify(data));
  if (request.status >= 200 && request.status < 400) {
    data.forEach(quote => {
      const card = document.createElement('div');
      card.setAttribute('class', 'card');

      const h1 = document.createElement('h1');
      h1.textContent = quote.author;

      const p = document.createElement('p');
      quote.quote = quote.quote.substring(0, 300);
      p.textContent = `${quote.quote}...`;

      container.appendChild(card);
      card.appendChild(h1);
      card.appendChild(p);
    });
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = `Gah, it's not working!`;
    app.appendChild(errorMessage);
  }
}

request.send();
