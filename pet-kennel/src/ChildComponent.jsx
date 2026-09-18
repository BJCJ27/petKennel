import React from 'react';

// A single pet card. It is "presentational": it only shows the props the
// parent gives it and calls the parent's onFeed callback when the button is
// clicked. All the real state lives in the parent (App.jsx).
class ChildComponent extends React.Component {
  constructor(props) {
    super(props);
    // Bind the handler so `this` refers to the component inside it.
    this.handleClick = this.handleClick.bind(this);
  }

  // 4. CHILD LOGIC — tell the parent which pet's button was clicked.
  handleClick() {
    this.props.onFeed(this.props.id);
  }

  render() {
    const { name, species, image, status, happiness, isHappy } = this.props;

    return (
      <div className={`card ${isHappy ? 'card--happy' : 'card--sad'}`}>
        <img className="card__img" src={image} alt={`${name} the ${species} looking ${status}`} />

        <h2 className="card__name">{name}</h2>
        <p className="card__species">{species}</p>

        <p className={`card__status ${isHappy ? 'is-happy' : 'is-sad'}`}>
          {isHappy ? '😊 Happy' : '😢 Hungry'}
        </p>

        {/* Happiness meter */}
        <div className="meter" aria-label={`Happiness ${happiness} percent`}>
          <div className="meter__fill" style={{ width: `${happiness}%` }} />
        </div>
        <span className="meter__label">{happiness}%</span>

        <button className="card__btn" onClick={this.handleClick}>
          🍖 Feed {name}
        </button>
      </div>
    );
  }
}

export default ChildComponent;
