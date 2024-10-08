const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static("src"));
app.get("/", (req, res) => res.sendFile("src", "index.html"));

app.listen(port, () => console.log("Listening on port ", port));
