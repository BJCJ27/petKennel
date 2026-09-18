import React, { Component } from 'react';
import ChildComponent from './ChildComponent';
import { initialData } from './data';
import './App.css';

// Below this happiness value a pet is "sad"; at or above it the pet is "happy".
const HAPPY_THRESHOLD = 50;

class App extends Component {
  constructor(props) {
    super(props);

    // 1. STATE — seed state from the data in data.js.
    this.state = {
      pets: initialData,
    };
  }

  // Lifecycle: once the app is on screen, pets slowly get hungry over time so
  // you can watch happy pets drift back to sad if you stop caring for them.
  componentDidMount() {
    this.timer = setInterval(this.getHungry, 2500);
  }

  // Lifecycle: clean up the timer so it never runs after the app unmounts.
  componentWillUnmount() {
    clearInterval(this.timer);
  }

  // Every tick, drop each pet's happiness a little (never below 0).
  getHungry = () => {
    this.setState((prev) => ({
      pets: prev.pets.map((pet) => ({
        ...pet,
        happiness: Math.max(0, pet.happiness - 5),
      })),
    }));
  };

  // 3. EVENT METHOD — feeding raises one pet's happiness (capped at 100).
  // This lives in the parent and is handed to each child through props.
  feedPet = (id) => {
    this.setState((prev) => ({
      pets: prev.pets.map((pet) =>
        pet.id === id
          ? { ...pet, happiness: Math.min(100, pet.happiness + 25) }
          : pet
      ),
    }));
  };

  render() {
    return (
      <div className="app">
        <header className="app__header">
          <h1>🐾 Happy Tails Kennel</h1>
          <p>Feed each pet to keep them happy. Ignore them and they get hungry!</p>
        </header>

        <div className="kennel">
          {/* 2. MAPPING — render a card for every pet in state. */}
          {this.state.pets.map((pet) => {
            const isHappy = pet.happiness >= HAPPY_THRESHOLD;
            return (
              <ChildComponent
                key={pet.id}
                id={pet.id}
                name={pet.name}
                species={pet.species}
                happiness={pet.happiness}
                // The parent picks the image + status from happiness and passes
                // them down; the child just displays whatever props it is given.
                image={isHappy ? pet.happyImage : pet.sadImage}
                status={isHappy ? 'Happy' : 'Hungry'}
                isHappy={isHappy}
                onFeed={this.feedPet}
              />
            );
          })}
        </div>
      </div>
    );
  }
}

export default App;
