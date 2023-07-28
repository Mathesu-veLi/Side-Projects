import User from '../models/User';

class UserController {
  async store(req, res) {
    try {
      const novoUser = await User.create(req.body);
      return res.json(novoUser);
    } catch (e) {
      return res.status(400).json({
        errors: e.errors.map(erro => erro.message),
      })
    };
  };

  async index(req, res) {
    try {
      const users = await User.findAll();
      return res.json(users)
    } catch(e) {
      return res.json(null);
    }
  }

  async show(req, res) {
    try {
      const user = await User.findByPk(req.params.id);
      if (!user) {
        return res.status(400).json({
          errors: ['ID inexistente']
        })
      }
      return res.json(user)
    } catch(e) {
      return res.status(400).json({
        errors: e.errors.map(erro => erro.message),
      })
    }
  }

  async update(req, res) {
    try {
      if(!req.params.id) {
        return res.status(400).json({
          errors: ['ID não enviado']
        })
      }

      const user = await User.findByPk(req.params.id);
      if(!user) {
        return res.status(400).json({
          errors: ['Usuário não existe']
        });
      }

      const novosDados = await user.update(req.body);

      return res.json(novosDados)
    } catch(e) {
      return res.status(400).json({
        errors: e.errors.map(erro => erro.message),
      })
    }
  }

};

export default new UserController();
