import User from '../models/User';

class UserController {
  async store(req, res) {
    const novoUser = await User.create({
      nome: 'Matheus',
      email: 'matheuslevit@gmail.com',
      password: 'vel'
    })
    res.json(novoUser);
  };
};

export default new UserController();
