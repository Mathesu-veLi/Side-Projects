import React from "react";
import PropTypes from "prop-types";
import { FaPlus } from "react-icons/fa";

import "./style.css";

export default function Form({ handleChanged, handleSubmit, newTask }) {
  return (
    <form onSubmit={handleSubmit} action="#" className="form">
      <input onChange={handleChanged} type="text" value={newTask} />
      <button type="submit">
        <FaPlus />
      </button>
    </form>
  );
}

Form.propTypes = {
  handleChanged: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  newTask: PropTypes.string.isRequired,
};
