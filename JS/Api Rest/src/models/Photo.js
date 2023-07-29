import Sequelize, { Model } from 'sequelize';

export default class Photo extends Model {
  static init(sequelize) {
    super.init({
      originalname: {
        type: Sequelize.STRING,
        defaultValue: '',
        validade: {
          notEmpty: {
            msg: 'Campo não pode ficar vazio'
          },
        },
      },

      filename: {
        type: Sequelize.STRING,
        defaultValue: '',
        validade: {
          notEmpty: {
            msg: 'Campo não pode ficar vazio'
          },
        },
      },

    }, {
      sequelize,
      tableName: 'photos'
    });
  };

  static associate(models) {
    this.belongsTo(models.Aluno, { foreignKey: 'aluno_id' });
  }
}
