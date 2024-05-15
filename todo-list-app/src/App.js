import React, { useState } from 'react';//imports react and the usestate(manage state)
import './App.css';//imports the css file
import TodoList from './TodoList';//imports the todolist.js file
import TodoForm from './TodoForm';//imports the todoform.js file inorder to add new todo lists

function App() {
  const [todos, setTodos] = useState([]);//defines the app functional component

  const addTodo = (text) => {
    const newTodos = [...todos, { text, completed: false }];
    setTodos(newTodos);
  };

  const toggleTodo = (index) => {
    const newTodos = [...todos];
    newTodos[index].completed = !newTodos[index].completed;
    setTodos(newTodos);
  };

  const deleteTodo = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <div className="App">
      <h1>To-Do List</h1>
      <TodoForm addTodo={addTodo} />
      <TodoList todos={todos} toggleTodo={toggleTodo} deleteTodo={deleteTodo} />
    </div>
  );
}

export default App;