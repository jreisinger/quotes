//https://github.com/taniarascia/sandbox/tree/master/ghibli

const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();

// Find out host and port
//request.open('GET', 'http://quotes.reisinge.net/api/v1/all/', true);
//request.open('GET', 'http://localhost:5000/api/v1/all/', true);
var host = "http://" + window.location.hostname + ":" + window.location.port;
var url  = host + "/api/v1/all/";

request.open('GET', url, true);

request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  var re = new RegExp("Matu|Elka|Dado|Dadko", "i");
  if (request.status >= 200 && request.status < 400) {
    data.forEach(quote => {
      if ( ! re.test(quote.author) ) {
         return;
      }

      const card = document.createElement('div');
      card.setAttribute('class', 'card');

      const h1 = document.createElement('h1');
      h1.textContent = quote.author;

      const p = document.createElement('p');
      //quote.quote = quote.quote.substring(0, 300);
      p.textContent = quote.quote;

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
