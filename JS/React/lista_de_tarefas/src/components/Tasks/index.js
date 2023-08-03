import React from "react";
import PropTypes from "prop-types";
import { FaEdit, FaWindowClose } from "react-icons/fa";

import "./style.css";

export default function Tasks({ tasks, handleEditTask, handleDeleteTask }) {
  return (
    <ul className="tasks">
      {tasks.map((task, index) => (
        <li key={index}>
          {task}
          <span>
            <FaEdit
              className="edit"
              onClick={(e) => handleEditTask(e, index)}
            />
            <FaWindowClose
              className="delete"
              onClick={(e) => handleDeleteTask(e, index)}
            />
          </span>
        </li>
      ))}
    </ul>
  );
}

Tasks.propTypes = {
  handleDeleteTask: PropTypes.func.isRequired,
  handleEditTask: PropTypes.func.isRequired,
  tasks: PropTypes.array.isRequired,
};
