import React from 'react';
import { FaHome, FaSignInAlt, FaUserAlt } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import { Nav } from './styled';

export default function Header() {
  // eslint-disable-next-line no-unused-vars
  const botaoClicado = useSelector(
    (state) => state.exampleReducer.botaoClicado,
  );

  return (
    <Nav>
      <Link to="/">
        <FaHome size={24} />
      </Link>
      <div>
        <Link to="/login">
          <FaUserAlt size={24} />
        </Link>
        <Link to="/">
          <FaSignInAlt size={24} />
        </Link>
        {botaoClicado ? 'Clicado' : 'Não clicado'}
      </div>
    </Nav>
  );
}
