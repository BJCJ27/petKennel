# AI Contribution Statement

## 1. Tools used

Claude (Anthropic, Opus 4.8), used through the Claude app. No other AI tools or
autocomplete were used.

## 2. Prompts

I asked it to help me complete the Pet Kennel assignment: filling in the
class-based `App.jsx` (state from `data.js`, a `feedPet` method, and rendering
the cards with `.map()`), completing `ChildComponent.jsx` so the card displays
its props and calls the parent's method on click, and creating the happy/sad
pet images. I also asked it to style the cards and to write up this README.
Along the way I asked it to run the app and show me screenshots so I could
confirm the feed button actually swapped the happy and sad faces.

## 3. What it got wrong

Two real things came up:

- **The import didn't match the filename.** The starter `App.jsx` imports
  `./ChildComponent`, but the provided file was named `childComponent.jsx` with a
  lowercase `c`. On a case-sensitive setup (and Vite) that import fails to
  resolve, so the app wouldn't run. We caught it because the dev server errored
  on the import, and fixed it by renaming the file to `ChildComponent.jsx`.
- **The starter image URLs were fake.** `data.js` shipped with placeholder links
  like `https://some-url.com/sad-yoda.jpg` that don't load anything. I replaced
  them with real SVG images stored in the project so the pets always show up.

## 4. Reflection

The biggest thing I learned is how state "lifts up": the parent owns the pet
data and the `feedPet` method, and the child only receives props and calls the
callback — it doesn't hold its own state. I also learned why you copy state with
`.map()` and the spread operator instead of mutating it directly, so React knows
to re-render. I can explain every line of the submission: how the constructor
seeds state from `data.js`, how `.map()` builds one card per pet, how clicking
the button in the child calls `this.props.onFeed(this.props.id)` back up to the
parent, and how the parent picks the happy or sad image from each pet's
happiness value.
