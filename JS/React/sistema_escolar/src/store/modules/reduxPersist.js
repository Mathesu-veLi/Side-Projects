import storage from 'redux-persist/lib/storage';
import { persistReducer } from 'redux-persist';

export default (reducers) => {
  const persistedReducers = persistReducer(
    {
      key: 'NOME_DA_APLICAÇÃO',
      storage,
      whitelist: ['exampleReducer'],
    },
    reducers,
  );

  return persistedReducers;
};
