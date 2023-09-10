import React from 'react';

import { Container } from '../../styles/GlobalStyle';
import { Form } from './styled';

export default function Login() {
  return (
    <Container>
      <h1>Login</h1>

      <Form onSubmit={handleSubmit}>
        <label htmlFor="email">
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Seu email"
          />
        </label>
        <label htmlFor="password">
          Senha:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Seu password"
          />
        </label>

        <button type="submit">Acessar</button>
      </Form>
    </Container>
  );
}
