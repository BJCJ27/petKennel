// Pet data for the kennel.
// Each pet ships with its own happy and sad image so nothing depends on a
// network connection. Vite turns each `import` of an .svg file into a URL
// string we can drop straight into an <img src={...} /> tag.
import dogHappy from './assets/pets/dog-happy.svg';
import dogSad from './assets/pets/dog-sad.svg';
import catHappy from './assets/pets/cat-happy.svg';
import catSad from './assets/pets/cat-sad.svg';
import bunnyHappy from './assets/pets/bunny-happy.svg';
import bunnySad from './assets/pets/bunny-sad.svg';
import foxHappy from './assets/pets/fox-happy.svg';
import foxSad from './assets/pets/fox-sad.svg';

// `happiness` is a 0-100 meter. The parent decides the mood from it:
// >= 50 shows the happy image, below 50 shows the sad image.
export const initialData = [
  {
    id: 1,
    name: 'Biscuit',
    species: 'Dog',
    happiness: 30,
    happyImage: dogHappy,
    sadImage: dogSad,
  },
  {
    id: 2,
    name: 'Mochi',
    species: 'Cat',
    happiness: 20,
    happyImage: catHappy,
    sadImage: catSad,
  },
  {
    id: 3,
    name: 'Clover',
    species: 'Bunny',
    happiness: 40,
    happyImage: bunnyHappy,
    sadImage: bunnySad,
  },
  {
    id: 4,
    name: 'Ember',
    species: 'Fox',
    happiness: 15,
    happyImage: foxHappy,
    sadImage: foxSad,
  },
];
