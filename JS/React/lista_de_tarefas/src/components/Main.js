import React, { Component } from "react";

import { FaPlus } from "react-icons/fa";
import "./Main.css";

export default class Main extends Component {
  state = {
    newTask: "",
  };

  handleChanged = (e) => {
    this.setState({
      newTask: e.target.value,
    });
  };

  render() {
    const { newTask } = this.state;
    return (
      <div className="main">
        <h1>Lista de Tarefas</h1>

        <form action="#" className="form">
          <input onChange={this.handleChanged} type="text" value={newTask} />
          <button type="submit">
            <FaPlus />
          </button>
        </form>
      </div>
    );
  }
}
