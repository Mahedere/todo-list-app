import React, { useState } from 'react'; //imports react and the usestate(manage state) & JSX components
import './App.css'; //imports the css file
import TodoList from './TodoList'; //imports the todolist.js file
import TodoForm from './TodoForm'; //imports the todoform.js file inorder to add new todo lists

function App() { //defines the app functional component
  const [todos, setTodos] = useState([]); //creating variable todos & setTodos

  const addTodo = (text) => { //defines function addTodo & parameter text
    const newTodos = [...todos, { text, completed: false }]; //creates a new array newTodos and new object 'text' & completed set to false
    setTodos(newTodos); //updates todos to the newTodos
  };

  const toggleTodo = (index) => { //defines function toggleTodo & parameter index
    const newTodos = [...todos]; //creates a new array newTodos a copy of the current todos array 
    newTodos[index].completed = !newTodos[index].completed; //if completed is true make false and vice versa
    setTodos(newTodos); //updates the new todos array
  };

  const deleteTodo = (index) => { //defines function deleteTodo & parameter index
    const newTodos = [...todos]; //creates a new array newTodos a copy of the current todos array
    newTodos.splice(index, 1); //removes one item from newtodos at the specified index :splice method modifies the array in place
    setTodos(newTodos); //updates the new todos array
  };

  return ( //JSX component return (describes what the UI looks like based on thios functionality)
    <div className="App">
      <h1>Mahi's To-Do List</h1>
      <TodoForm addTodo={addTodo} />
      <TodoList todos={todos} toggleTodo={toggleTodo} deleteTodo={deleteTodo} />
    </div>
  );
}

export default App;//exports the toogleTodo & deleteTodo functions