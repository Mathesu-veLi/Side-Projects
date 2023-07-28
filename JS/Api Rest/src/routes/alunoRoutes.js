import { Router } from 'express';
import alunoController from '../controllers/AlunoController';

const router = new Router();

router.get('/', alunoController.index);
router.get('/', alunoController.show);
router.post('/:id', alunoController.store);
router.put('/:id', alunoController.update);
router.delete('/:id', alunoController.delete);

export default router;
