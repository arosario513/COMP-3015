import express, { Express, Request, Response } from "express";
import path from "path";
const app: Express = express();
const port = process.env.PORT || 3000;

app.use(express.static("src"));

app.get("/", (req: Request, res: Response) => {
    res.sendFile(path.resolve("src", "index.html"));
});

app.listen(port, () => console.log("Listening on port ", port));
