import React, { Component } from "react";

import { FaEdit, FaPlus, FaWindowClose } from "react-icons/fa";
import "./Main.css";

export default class Main extends Component {
  state = {
    newTask: "",
    tasks: [],
    index: -1,
  };

  handleChanged = (e) => {
    this.setState({
      newTask: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const { tasks, index } = this.state;
    let { newTask } = this.state;
    newTask = newTask.trim();

    if (tasks.indexOf(newTask) !== -1 || newTask === "") return;
    const newTasks = [...tasks];

    if (index === -1) {
      this.setState({
        tasks: [...newTasks, newTask],
        newTask: "",
      });
    } else {
      newTasks[index] = newTask;

      this.setState({
        tasks: [...newTasks],
        index: -1,
      });
    }
  };

  handleEditTask = (e, index) => {
    const { tasks } = this.state;
    this.setState({
      index,
      newTask: tasks[index],
    });
  };

  handleDeleteTask = (e, index) => {
    const { tasks } = this.state;
    let newTasks = [...tasks];
    newTasks.splice(index, 1);

    this.setState({
      tasks: [...newTasks],
    });
  };

  render() {
    const { newTask, tasks } = this.state;
    return (
      <div className="main">
        <h1>Lista de Tarefas</h1>

        <form onSubmit={this.handleSubmit} action="#" className="form">
          <input onChange={this.handleChanged} type="text" value={newTask} />
          <button type="submit">
            <FaPlus />
          </button>
        </form>

        <ul className="tasks">
          {tasks.map((task, index) => (
            <li key={index}>
              {task}
              <span>
                <FaEdit
                  className="edit"
                  onClick={(e) => this.handleEditTask(e, index)}
                />
                <FaWindowClose
                  className="delete"
                  onClick={(e) => this.handleDeleteTask(e, index)}
                />
              </span>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}
