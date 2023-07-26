import Aluno from '../models/Aluno';

class HomeController {
  async index(req, res) {
    const novoAluno = await Aluno.create({
      nome: 'Matheus',
      sobrenome: 'Fernandes',
      email: 'matheuslevit@gmail.com',
      idade: 13,
      peso: 51,
      altura: 1.54
    })
    res.json(novoAluno);
  };
};

export default new HomeController();
