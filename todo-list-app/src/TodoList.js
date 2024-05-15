import React from 'react';

function TodoList({ todos, toggleTodo, deleteTodo }) { //defines Todolist then recieves 3 props 
  return ( //jsx to map over the todos 
    <ul>
      {todos.map((todo, index) => (
        <li key={index} style={{ textDecoration: todo.completed ? 'line-through' : '' }}> 
        {/*the index is to know which item has been changed/added/removed and the style does a crossed out when completed*/}
          <span onClick={() => toggleTodo(index)}>{todo.text}</span>
          {/*displays the text & allows to toggle completion status */}
          <button onClick={() => deleteTodo(index)}>Delete</button>
          {/*creates a button to delete */}
        </li>
      ))}
    </ul>
  );
}

export default TodoList;