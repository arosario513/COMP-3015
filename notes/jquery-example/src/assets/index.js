$(() => {
    let darkMode = false;
    $("button#toggle-text").on("click", () => {
        $(".txt").toggle();
    });
    $("button#change-theme").on("click", () => {
        if (!darkMode) {
            $("body").css({ "background-color": "#101010", color: "white" });
            $("main").css({ "background-color": "#202020" });
            darkMode = true;
        } else {
            $("body").css({ "background-color": "#f0f0ff", color: "black" });
            $("main").css({ "background-color": "white" });
            darkMode = false;
        }
    });
});
