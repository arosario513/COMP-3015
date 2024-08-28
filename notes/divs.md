# The div tag

## What is it?

The div tag is used as a generic container which groups content, and makes styling the content inside it easier.

## Example

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title>Website</title>
  </head>
  <body>
    <div class="head-title">
      <h1>Website</h1>
    </div>

    <div class="main-content">
      <h3>Hello World</h3>
      <p>Welcome to my website!</p>
    </div>
  </body>
</html>
```

Instead of having to style each tag one by one, you can wrap all of it inside divs and set a class on it, then style the div itself.

## Things to consider

You don't need to use div for everything you can use tags like header, footer, nav, figure, main and section. Use div only when it's necessary.
