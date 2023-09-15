import React, { useState } from 'react';
import { get } from 'lodash';
import { isEmail, isInt, isFloat } from 'validator';
import PropTypes from 'prop-types';
import { toast } from 'react-toastify';

import { Container } from '../../styles/GlobalStyle';
import { Form } from './styled';
import { useParams } from 'react-router-dom';

export default function Aluno() {
  const { id } = useParams();
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState('');
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    let formErros = false;

    if (name.length < 3 || name.length > 255) {
      formErros = true;
      toast.error('Nome precisa ter entre 3 e 255 caracteres');
    }

    if (surname.length < 3 || surname.length > 255) {
      formErros = true;
      toast.error('Sobrenome precisa ter entre 3 e 255 caracteres');
    }

    if (!isEmail(email)) {
      formErros = true;
      toast.error('Email inválido');
    }

    if (!isInt(String(age))) {
      toast.error('Idade inválida');
      formErros = true;
    }

    if (!isFloat(String(weight))) {
      toast.error('Peso inválido');
      formErros = true;
    }
    if (!isFloat(String(height))) {
      toast.error('Altura inválida');
      formErros = true;
    }
  };

  return (
    <Container>
      <h1>{id ? 'Editar aluno' : 'Novo aluno'}</h1>

      <Form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Nome"
        />
        <input
          type="text"
          value={surname}
          onChange={(e) => setSurname(e.target.value)}
          placeholder="Sobrenome"
        />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />
        <input
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          placeholder="Idade"
        />
        <input
          type="text"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          placeholder="Peso"
        />
        <input
          type="text"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          placeholder="Altura"
        />

        <button type="submit">Enviar</button>
      </Form>
    </Container>
  );
}
