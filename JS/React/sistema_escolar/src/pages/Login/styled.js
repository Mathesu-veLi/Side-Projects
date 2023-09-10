import styled from 'styled-components';

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  margin: 10px 0 10px 0;

  label {
    display: flex;
    flex-direction: column;
    margin: 10px 0 10px 0;
  }

  input {
    margin: 5px 0 5px 0;
    padding: 10px;
    font-size: 1.03em;
    border: 1px solid #7e7e7e;
    border-radius: 5px;
  }

  input:focus {
    border: 1px solid #af2f2f;
  }
`;
