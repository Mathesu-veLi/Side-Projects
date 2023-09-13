import React from 'react';
import { get } from 'lodash';
import PropTypes from 'prop-types';

import { Container } from '../../styles/GlobalStyle';

export default function Aluno({ match }) {
  const id = get(match, 'params.id', 0);

  return (
    <Container>
      <h1>Aluno</h1>
    </Container>
  );
}

Aluno.propTypes = {
  match: PropTypes.shape({}),
};
