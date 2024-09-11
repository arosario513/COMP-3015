const express = require("express");
const path = require("path");
const app = express();
const port = process.env.PORT || 3000;
app.use(express.static(path.resolve("src")));
app.get("/", (req, res) => res.sendFile("src", "index.html"));
app.get("/*", (req, res) => res.status(404).send("Page not found"));
app.listen(port, () => console.log("Listening on port ", port));
