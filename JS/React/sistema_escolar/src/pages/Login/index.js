import React from 'react';
import { useDispatch } from 'react-redux';

import { Container } from '../../styles/GlobalStyle';
import { Title, P } from './styled';
import * as exampleActions from '../../store/modules/example/actions';

export default function Login() {
  const dispatch = useDispatch();

  function handleClick(e) {
    e.preventDefault();

    dispatch(exampleActions.clicaBotãoRequest());
  }

  return (
    <Container>
      <Title isRed={true}>Login</Title>
      <P>Lorem ipsum dolor sit amet.</P>
      <button type="button" onClick={handleClick}>
        Enviar
      </button>
    </Container>
  );
}
