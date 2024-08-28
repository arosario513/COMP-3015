# HTML Tags

## Basic Structure Example

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Website</title>
    <link href="assets/style.css" rel="stylesheet" />
</head>

<body>
    <header>
        <nav>
            <a>Website</a>
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/faq">FAQ</a>
        </nav>
    </header>

    <main>
        <section>
            <h1>Welcome to my website!</h1>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
                minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                aliquip ex ea commodo consequat. Duis aute irure dolor in
                reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
                culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Website</p>
    </footer>
    <script src="assets/index.js"></script>
</body>

</html>
```

| Tag     | Function                                      |
| ------- | --------------------------------------------- |
| doctype | Tells the browser what type of file to expect |
| html    | Contains everything                           |
| head    | Contains the metadata of the file             |
| meta    | Defines the metadata                          |
| body    | Has all the content that will be shown        |
| h1 - h6 | Heading text                                  |
| p       | Paragraph                                     |
| a       | Used for hyperlinks                           |

The header, footer, main, and section tags don't impact the look of the page and only help with readability of the html file

## Lists

```
...
<section>
    <h1>Fruits</h1>
    <ul>
        <li>Apple</li>
        <li>Pear</li>
        <li>Fruits</li>
    </ul>
</section>
...
```

| Tag | Function                  |
| --- | ------------------------- |
| ul  | defines an unordered list |
| ol  | defines an ordered list   |
| li  | list item                 |
