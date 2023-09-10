import styled from 'styled-components';

export const AlunoContainer = styled.div`
  margin-top: 20px;

  table {
    width: 100%;
    border-spacing: 10px;
    border-collapse:collapse
  }

  th {
    padding-bottom: 15px;
  }

  td {
    padding: 10px 0;
  }

  table tr:not(.thead) + tr {
    border-top: 1px solid #afafaf;
  }

  td * {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #name {
    width: 40%;
  }
`;

export const ProfilePicture = styled.div`
  img {
    width: 36px;
    height: 36px;
    border-radius: 50%;
  }
`;
