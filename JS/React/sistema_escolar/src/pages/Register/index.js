import React, { useState } from 'react';
import { toast } from 'react-toastify';
import { isEmail } from 'validator';

import { Container } from '../../styles/GlobalStyle';
import { Form } from './styled';
import axios from '../../services/axios';

export default function Register() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    let formErros = false;

    if (nome.length < 3 || nome.length > 255) {
      formErros = true;
      toast.error('Nome deve ter entre 3 e 255 caracteres');
    }

    if (!isEmail(email)) {
      formErros = true;
      toast.error('Email inválido');
    }

    if (password.length < 6 || password.length > 50) {
      // eslint-disable-next-line no-unused-vars
      formErros = true;
      console.log(password.length);
      toast.error('Senha deve ter entre 6 e 50 caracteres');
    }
  }

  return (
    <Container>
      <h1>Criar conta</h1>

      <Form onSubmit={handleSubmit}>
        <label htmlFor="nome">
          Nome:
          <input
            type="text"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            placeholder="Seu nome"
          />
        </label>
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
            placeholder="Sua senha"
          />
        </label>

        <button type="submit">Criar minha conta</button>
      </Form>
    </Container>
  );
}
