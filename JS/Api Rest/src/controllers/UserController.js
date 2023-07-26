import User from '../models/User';

class UserController {
  async store(req, res) {
    try {
      const novoUser = await User.create({
        nome: 'Matheus',
        email: 'matheuslevit@gmail.com',
        password: 'veli15'
      })
      res.json(novoUser);
    } catch(e) {
      res.status(400).json(e.errors.map(erro => erro.message))
    };
  };
};

export default new UserController();
