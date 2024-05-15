import React, { useState } from 'react';

function TodoForm({ addTodo }) { // defines function TodoForm & recieves a single prop 'addTodo'
  const [value, setValue] = useState(''); // initializes state

  const handleSubmit = (e) => { //defines function handleSubmit
    e.preventDefault(); //prevents the default behaviour not to cause reload
    if (!value) return;//checks if input value is empty if so returns early & prevents an empty todo being added
    addTodo(value); //calls the addTodo function with the current value
    setValue(''); //resets the input field empty after form subbmitted
  };

  return ( // a jsx that creates a form after submission
    <form onSubmit={handleSubmit}>
        {/* creates a form element and runs when submitted*/}
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Add a new to-do"
      />
      <button type="submit">Add</button>
    </form>
  );
}

export default TodoForm;