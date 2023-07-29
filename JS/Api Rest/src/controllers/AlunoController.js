import Aluno from '../models/Aluno';

class AlunoController {
  async index(req, res) {
    const alunos = await Aluno.findAll({ attributes: ['id', 'nome', 'sobrenome', 'email', 'idade', 'peso', 'altura'] });
    return res.json(alunos);
  };

  async show(req, res) {
    try {
      const { id } = req.params;
      if (!id) {
        return res.status(400).json({
          errors: ['Faltando ID'],
        });
      };

      const aluno = await Aluno.findByPk(id);

      if (!aluno) {
        return res.status(400).json({
          errors: ['Aluno não existe'],
        });
      };

      const {nome, sobrenome, email, idade, peso, altura} = aluno

      return res.json({id, nome, sobrenome, email, idade, peso, altura});
    } catch (e) {
      return res.status(400).json({
        errors: e.errors.map(err => err.message)
      });
    };
  };

  async store(req, res) {
    try {
      const aluno = await Aluno.create(req.body)
      const {id, nome, sobrenome, email, idade, peso, altura} = aluno

      return res.json({id,nome, sobrenome, email, idade, peso, altura})
    } catch (e) {
      return res.status(400).json({
        errors: e.errors.map(err => err.message)
      });
    }
   };

  async update(req, res) {
    try {
      const { id } = req.params;
      if (!id) {
        return res.status(400).json({
          errors: ['Faltando ID'],
        });
      };

      const aluno = await Aluno.findByPk(id);

      if (!aluno) {
        return res.status(400).json({
          errors: ['Aluno não existe'],
        });
      };

      const alunoAtualizado = await aluno.update(req.body);
      const {nome, sobrenome, email, idade, peso, altura} = alunoAtualizado;

      return res.json({nome, sobrenome, email, idade, peso, altura});
    } catch (e) {
      return res.status(400).json({
        errors: e.errors.map(err => err.message)
      });
    };
  };

  async delete(req, res) {
    try {
      const { id } = req.params;
      if (!id) {
        return res.status(400).json({
          errors: ['Faltando ID'],
        });
      };

      const aluno = await Aluno.findByPk(id);

      if (!aluno) {
        return res.status(400).json({
          errors: ['Aluno não existe'],
        });
      };

      await aluno.destroy();
      return res.json('Aluno deletado com sucesso');
    } catch (e) {
      return res.status(400).json({
        errors: e.errors.map(err => err.message)
      });
    };
  };
};

export default new AlunoController();
