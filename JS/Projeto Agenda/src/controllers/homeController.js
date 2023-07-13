const Contato = require('../models/ContatoModel');

exports.index = async (req, res) => {
    try {
        contatos = await Contato.buscaContatos(req.session.user.email);
    } catch (e) {
        contatos = await Contato.buscaContatos('');
    }
    
    res.render('index', { contatos });
};