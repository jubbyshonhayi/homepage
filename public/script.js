// Inspiration quote button
const button = document.getElementById("quote-btn");

if (button){

    button.addEventListener("click", function(){

        // List of quotes displayed randomly
        const quotes = [
            "Ideas become reality when you build them.",
            "Discipline beats motivation.",
            "Learn, build, improve, repeat.",
            "Technology creates opportunities.",
            "Great businesses solve real problems."
        ];


        // Select a random quote
        const random = quotes[Math.floor(Math.random() * quotes.length)];

        document.getElementById("quote").innerHTML = random;
    });
}

