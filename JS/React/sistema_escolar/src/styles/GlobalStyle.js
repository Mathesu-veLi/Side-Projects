import styled, { createGlobalStyle } from 'styled-components';
import * as colors from '../config/colors';
import 'react-toastify/dist/ReactToastify.css';

export default createGlobalStyle`
    * {
      margin: 0;
      padding: 0;
      outline: none;
      box-sizing: border-box;
    }

    body {
      font-family: sans-serif;
      background-color: ${colors.primaryDarkColor};
    }

    html, body, #root {
      height: 100%;
    }

    button {
      cursor: pointer;
      background-color: ${colors.primaryColor};
      border: none;
      color: #efefef;
      padding: 10px 20px;
      border-radius: 4px;
      font-weight: 700;
    }

    a {
      text-decoration: none;
      color: ${colors.primaryColor};
    }

    ul {
      list-style: none;
    }
`;

export const Container = styled.section`
  max-width: 360px;
  background-color: #ddd;
  margin: 30px auto;
  padding: 30px;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4);
`;
