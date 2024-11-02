$(document).ready(function() {
    const totalPairs = 8; // Número de pares
    let attempts = 0;
    let pairsFound = 0;
    let completedGames = 0;
    function initializeGame() {
        attempts = 0;
        pairsFound = 0;
        $("#attempts").text(`Tries: ${attempts}`);
        $("#pairs-found").text(`Pairs Found: ${pairsFound}`);
        $("#efficiency").text(`Efficiency: 0%`);
        createCards();
    }
    function createCards() {
        $("#game-board").empty();
        let characters = ["A", "B", "C", "D", "E", "F", "G", "H"];
        characters = [...characters, ...characters];
        characters.sort(() => 0.5 - Math.random());
        characters.forEach((character, index) => {
            $("#game-board").append(
                `<div class="card" data-character="${character}"
id="card${index}">${character}</div>`,
            );
        });
        $(".card").on("click", cardClickHandler);
    }
    let flippedCards = [];
    function cardClickHandler() {
        if ($(this).hasClass("flipped") || $(this).hasClass("matched")) return;
        $(this).text($(this).data("character")).addClass("flipped");
        flippedCards.push($(this));
        if (flippedCards.length === 2) {
            checkForMatch();
        }
    }
    function checkForMatch() {
        attempts++;
        $("#attempts").text(`Intentos: ${attempts}`);
        const [card1, card2] = flippedCards;
        if (card1.data("character") === card2.data("character")) {
            card1.addClass("matched");
            card2.addClass("matched");
            pairsFound++;
            $("#pairs-found").text(`Pairs Found:
${pairsFound}`);
            if (pairsFound === totalPairs) {
                completedGames++;
                $("#completed-games").text(`Games Completed:
${completedGames}`);
                alert("Game Completed");
            }
        } else {
            setTimeout(() => {
                card1.removeClass("flipped").text("");
                card2.removeClass("flipped").text("");
                alert("Try again.");
            }, 500);
        }
        updateEfficiency();
        flippedCards = [];
    }
    function updateEfficiency() {
        const efficiency = Math.round((pairsFound / attempts) * 100);
        $("#efficiency").text(`Efficiency: ${isNaN(efficiency) ? 0 : efficiency}%`);
    }
    $("#reload-game").click(function() {
        initializeGame();
    });
    initializeGame();
});
