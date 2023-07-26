import Sequelize, { Model } from 'sequelize';
import { defaultValueSchemable } from 'sequelize/types/utils';

export default class User extends Model {
  static init(sequelize) {
    super.init({
      nome: {
        type: Sequelize.STRING,
        defaultValue: '',
        validate: {
          len: {
            args: [3, 255],
            msg: 'Campo nome deve ter entre 3 e 255 caracteres'
          },

        }
      },
      email: Sequelize.STRING,
      password_hash: Sequelize.STRING,
      password: Sequelize.VIRTUAL,
    }, {
      sequelize,
    });
    return this;
  }
}
