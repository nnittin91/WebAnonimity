
var APIUrl = "http://localhost:5000/search?id="
document.addEventListener("click", function(e) {

  if (e.target.classList.contains("btn")) {
    var chosenPage = APIUrl + document.getElementById("searchForm").elements[0].value;
    // browser.tabs.create({
    //   url: chosenPage
    // });
    chosenPage = chosenPage.trim()
    var data = null;

    var xhr = new XMLHttpRequest();

    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        console.log(this.responseText);
        browser.windows.create({
            url: this.responseText,
            incognito : true
          });
      }
    });

    xhr.open("GET", chosenPage);

    xhr.send(data);

  }

});

