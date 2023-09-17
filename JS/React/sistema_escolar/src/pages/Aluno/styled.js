import styled from 'styled-components';
import { primaryColor } from '../../config/colors';

export const Form = styled.form`
  margin-top: 20px;
  display: flex;
  flex-direction: column;

  input {
    height: 40px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 0 10px;
  }
`;

export const ProfilePicture = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 50px 0;
  position: relative;

  img {
    border-radius: 50%;
    width: 180px;
    height: 180px;
  }

  a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    border: none;
    position: absolute;
    color: rgba(0, 0, 0, 0);
  }
  a:hover {
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
  }
`;
