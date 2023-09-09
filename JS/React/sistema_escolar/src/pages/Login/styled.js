import styled from 'styled-components';

export const Title = styled.h1`
  color: ${(props) => (props.isRed ? 'red' : 'blue')}
`;

export const P = styled.p`
  color: #000;
`;
